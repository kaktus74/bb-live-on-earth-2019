from picamera import PiCamera
from datetime import datetime
import time
import os
from os.path import split
from os.path import isdir
import ephem
from datetime import datetime, timezone

nazwa = 'ISS (ZARYA)'
line1='1 25544U 98067A   20014.55106447  .00001081  00000-0  27319-4 0  9995'
line2='2 25544  51.6449  33.6082 0005001 130.1836   8.0955 15.49563139208048'

iss = ephem.readtle(nazwa, line1, line2)

cam =  PiCamera()
cam.start_preview()

while True:
    t = datetime.now()
    iss.compute()
    lat = 32
    lon = 76
    fname = '{0}{1}{2}-Iss.jpg'.format(datetime.now(), lat, lon)
    print('Robię zdjęcie...')
    cam.capture(fname)
    print('Zdjęcie zapisane w pliku {0}'.format(fname))
    time.sleep(30)
    
cam.stop_preview()


