from datetime import datetime
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time
import csv
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
    

start = datetime.now()
# czas startu

nazwa = 'ISS (ZARYA)'
line1=''
line2=''
# dane do obliczenia pozycji

measured_distance = 0.56
measured_fov = 0.225

interval = co_ile (dl_maly_bok (tales (measured_distance, measured_fov))) / 2

#flight_duration = 180*60

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

czas_trwania = datetime.now() - start

with open('{0}/magnetic_field.txt'.format (my_dir), 'w') as f:
    writer = csv.writer(f)
    header = ['Date/Time', 'Compass X', 'Compass Y', 'Compass Z']
    writer.writerow (header)
    while czas_trwania.total_seconds () < flight_duration:
        print('Obliczam pozycje i zapisuje razem ze zdjeciem')
        print('Zapisuje pole magnetyczne')
        row = [datetime.now(), compass ['x'], compass ['y'], compass ['z']]
        writer.writerow (row)
        czas_trwania = datetime.now() - start
        time.sleep (interval)
    
