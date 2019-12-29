from datetime import datetime
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time

start = datetime.now()
# czas startu

nazwa = 'ISS (ZARYA)'
line1=''
line2=''
# dane do obliczenia pozycji

czas_trwania = datetime.now() - start
while czas_trwania.total_seconds() < 10800:
	print('Obliczam pozycje i zapisuje razem ze zdjeciem')
	time.sleep(1)
	print('Zapisuje pole magnetyczne')
	time.sleep(1)
	czas_trwania = datetime.now() - start
