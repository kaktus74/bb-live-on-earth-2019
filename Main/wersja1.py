from datetime import datetime
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time

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

interval = co_ile (dl_maly_bok (tales (0.56, 0.225))) / 2

#flight_duration = 180*60

flight_duration = 60

czas_trwania = datetime.now() - start
while czas_trwania.total_seconds() < flight_duration:
    print('Obliczam pozycje i zapisuje razem ze zdjeciem')
    time.sleep(1)
    print('Zapisuje pole magnetyczne')
    time.sleep(1)
    czas_trwania = datetime.now() - start
