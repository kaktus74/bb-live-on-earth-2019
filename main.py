from datetime import datetime, timezone
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time
from ephem import readtle, degree
from sense_hat import SenseHat
import csv
from logzero import logger, logfile
import reverse_geocoder as rg
sense=SenseHat()

name = 'ISS (ZARYA)'
line1='1 25544U 98067A   20014.55106447  .00001081  00000-0  27319-4 0  9995'
line2='2 25544  51.6449  33.6082 0005001 130.1836   8.0955 15.49563139208048'
# dane do obliczenia pozycji
iss = readtle(name, line1, line2)

def tales (h1, p1, h2 = 408000):
    p2 = p1 * (h2 / h1)
    return p2

def co_ile (pole_widzenia_m, czas_obiegu_s = 5400, obwod_m = 40075000):
    ile_razy = obwod_m / pole_widzenia_m
    co_ile = czas_obiegu_s / ile_razy
    return co_ile

def dl_maly_bok (dlugi_bok, aspekt = 16/9):
    maly_bok = dlugi_bok  / aspekt
    return maly_bok

def angle2exifRef(issAngle, directions):
    issLonstr = str(issAngle).split(':')
    issLonAngle2 = [float(z) for z in issLonstr]
    if issLonAngle2 [0] < 0:
        return directions [0]
    else:
        return directions [1]

def na_ulamki(x):
    x [0] = abs (x[0])
    x_exif = []
    x_exif.append(str (int (x[0])))
    x_exif.append(str (int (x [1])))
    x_exif.append(str (int (x [2]*10)))
    x_exif[0] += '/1'
    x_exif[1] += '/1'
    x_exif[2] += '/10'
    napis = x_exif[0] + ' ' + x_exif[1] + ' ' + x_exif[2]
    return napis


def angle2exif(issLon):
    isssublong = str(issLon).split(':')
    isssublong = [float(i) for i in isssublong]
    return na_ulamki (isssublong)

def picture (lat, lon, mydir):
    cam.exif_tags['IFD0.Copyright'] = "Black_Boxes"
    cam.exif_tags['GPS.GPSLatitudeRef'] = angle2exifRef(iss.sublat, ['S', 'N'])
    cam.exif_tags['GPS.GPSLatitude'] = angle2exif(iss.sublat)
    cam.exif_tags['GPS.GPSLongitudeRef'] = angle2exifRef (iss.sublong, ['W', 'E'])
    cam.exif_tags['GPS.GPSLongitude'] = angle2exif (iss.sublong) 
    fname = '{3}/{0},{1},{2}-Iss.jpg'.format(datetime.now(), lat, lon, mydir)
    cam.capture(fname)
    logger.info('Zapisalem zdjecie pod nazwa {0}'.format(fname))

def place ():
    pos = (iss.sublat / degree, iss.sublong / degree)
    location = rg.search(pos,mode=1)
    return location

def pixel1 ():
    x = [255, 10, 10]
    y = [10, 10, 255]
    z = [255, 255, 175]
    obrazek1 = [
        z, z, x, z, z, x, z, z,
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, z, z,
        z, z, z, z, z, z, z, z,
        z, z, y, z, z, y, z, z,
        z, z, z, y, y, z, z, z]
    sense.set_pixels(obrazek1)

def pixel2 ():
    x = [1, 1, 1]
    y = [255, 255, 255]
    obrazek2 = [
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        y, x, x, x, x, x, x, y,
        x, y, x, x, x, x, y, x,
        y, y, x, x, x, x, y, y,
        y, y, x, x, x, x, y, y,
        y, y, y, y, y, y, y, y
        ]
    sense.set_pixels(obrazek2)

def pixel3 ():
    x = [30, 255, 30]
    y = [255, 30, 30]
    z = [170, 170, 255]
    obrazek3 = [
        z, z, z, z, z, z, z, z,
        z, z, x, x, z, z, z, z,
        z, y, z, z, x, z, z, z,
        z, z, z, z, x, z, z, z,
        z, z, z, x, z, z, z, z,
        z, z, x, z, z, z, z, z,
        z, z, x, z, z, z, z, x,
        z, z, z, x, x, x, x, z,
        ]
    sense.set_pixels(obrazek3)

def pixel4 ():
    y = [1, 1, 80]
    x = [255, 255, 80]
    obrazek4 = [
        y, y, y, x, y, y, x, x,
        y, x, y, y, y, x, y, x,
        x, y, y, y, y, y, y, y,
        y, y, y, x, y, y, x, y,
        y, x, y, y, y, y, y, x,
        y, y, y, y, y, y, x, y,
        y, y, x, y, x, y, y, y,
        x, y, y, y, y, y, x, y
        ]
    sense.set_pixels(obrazek4)

start = datetime.now()
# czas startu

measured_distance = 0.56
measured_fov = 0.225

interval = co_ile (dl_maly_bok (tales (measured_distance, measured_fov))) / 2

#flight_duration = 180*60
flight_duration = 10800

czas_trwania = datetime.now() - start

my_dir = split (__file__)
my_dir = list (my_dir [:-1])
if my_dir [0] == '':
    my_dir [0] = '.'
my_dir = '/'.join ([str (i) for i in my_dir])
my_dir = my_dir + '/data'

if isdir (my_dir) == False:
    os.mkdir (my_dir)
logger.info (__file__)
logger.info (my_dir)

t = datetime.now(timezone.utc)
iss.compute(t)
logfile(my_dir + "/rotating-logfile.log")
logger.info('To powinno isc do pliku')
logger.info("{0} To jest interval".format(interval))
cam = PiCamera()
cam.start_preview()
logger.info("{0} To jest interval".format(interval))
pixels = 0
try:
    with open('{0}/magnetic_field.txt'.format (my_dir), 'w') as f:
        writer = csv.writer(f)
        header = ['Date/Time', 'Compass X', 'Compass Y', 'Compass Z']
        writer.writerow (header)
        sense.clear()
        while czas_trwania.total_seconds () < flight_duration:
            try:
                if pixels == 0:
                    pixel2()
                    pixels = pixels + 1
                elif pixels == 1:
                    pixel3()
                    pixels = pixels +1
                elif pixels == 2:
                    pixel1()
                    pixels = pixels +1
                else:
                    pixel4()
                    pixels = pixels -3
                compass = sense.compass_raw
                logger.info('Obliczam pozycje i zapisuje razem ze zdjeciem')
                picture (iss.sublat, iss.sublong, my_dir)
                logger.info('Zapisuje pole magnetyczne')
                row = [datetime.now(), compass ['x'], compass ['y'], compass ['z']] 
                writer.writerow (row)
                logger.info ('Jestesmy nad {0}'.format (place()))
                time.sleep (interval)
            except Exception as bum:
                logger.exception(bum)
            finally:
                czas_trwania = datetime.now() - start
finally:
    logger.info('stopping camera')
    cam.stop_preview()
    sense.clear()
