from picamera import PiCamera
from datetime import datetime
import time
import os
from os.path import split
from os.path import isdir
import ephem
from datetime import datetime, timezone
from time import sleep

name = 'ISS (ZARYA)'
line1='1 25544U 98067A   20014.55106447  .00001081  00000-0  27319-4 0  9995'
line2='2 25544  51.6449  33.6082 0005001 130.1836   8.0955 15.49563139208048'

iss = ephem.readtle(name, line1, line2)

cam =  PiCamera()
cam.start_preview()
sleep(3)

def picture (lat, lon):
    t = datetime.now()
    cam.exif_tags['IFD0.Copyright'] = "Black_Boxes"
    fname = '{0},{1},{2}-Iss.jpg'.format(datetime.now(), lat, lon)
    cam.capture(fname)
    print('Zapisalem zdjecie pod nazwa {0}'.format(fname))
    sleep(23)

l = 0

while l < 4:
    picture(46, 267)
    l = l + 1

cam.stop_preview()
print('Koniec')
