from datetime import datetime, timezone
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time
import ephem
from sense_hat import SenseHat
sense = SenseHat ()

def tales (h1, p1, h2 = 400000):
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

def picture (lat, lon):
    t = datetime.now()
    cam.exif_tags['IFD0.Copyright'] = "Black_Boxes"
    cam.exif_tags['GPS.GPSLatitudeRef'] = angle2exifRef(iss.sublat, ['S', 'N'])
    cam.exif_tags['GPS.GPSLatitude'] = angle2exif(iss.sublat)
    cam.exif_tags['GPS.GPSLongitudeRef'] = angle2exifRef (iss.sublong, ['W', 'E'])
    cam.exif_tags['GPS.GPSLongitude'] = angle2exif (iss.sublong) 
    fname = '{0},{1},{2}-Iss.jpg'.format(datetime.now(), lat, lon)
    cam.capture(fname)
    print('Zapisalem zdjecie pod nazwa {0}'.format(fname))


start = datetime.now()
# czas startu

name = 'ISS (ZARYA)'
line1='1 25544U 98067A   20014.55106447  .00001081  00000-0  27319-4 0  9995'
line2='2 25544  51.6449  33.6082 0005001 130.1836   8.0955 15.49563139208048'
# dane do obliczenia pozycji

iss = ephem.readtle(name, line1, line2)

measured_distance = 0.56
measured_fov = 0.225

interval = co_ile (dl_maly_bok (tales (measured_distance, measured_fov))) / 2

#flight_duration = 180*60

flight_duration = 15

czas_trwania = datetime.now() - start
##while czas_trwania.total_seconds() < flight_duration:
##    print('Obliczam pozycje i zapisuje razem ze zdjeciem')
##    time.sleep(interval)
##    print('Zapisuje pole magnetyczne')
##    czas_trwania = datetime.now() - start

my_dir = split (__file__)
my_dir = list (my_dir [:-1])
my_dir = '/'.join ([str (i) for i in my_dir])

my_dir = my_dir + '/../data'
if isdir (my_dir) == False:
    os.mkdir (my_dir)
print (__file__)
print (my_dir)

compass = sense.compass_raw

flight_duration = 15

cam =  PiCamera()
cam.start_preview()

t = datetime.now(timezone.utc)
iss.compute(t)

picture (iss.sublat, iss.sublong)

czas_trwania = datetime.now() - start
def main_function ():
    with open('{0}/magnetic_field.txt'.format (my_dir), 'w') as f:
        writer = csv.writer(f)
        header = ['Date/Time', 'Compass X', 'Compass Y', 'Compass Z']
        writer.writerow (header)
        while czas_trwania.total_seconds () < flight_duration:
            print('Obliczam pozycje i zapisuje razem ze zdjeciem')
            picture (iss.sublat, iss.sublong)
            print('Zapisuje pole magnetyczne')
            row = [datetime.now(), compass ['x'], compass ['y'], compass ['z']]
            writer.writerow (row)
            czas_trwania = datetime.now() - start
            time.sleep (interval)
    

