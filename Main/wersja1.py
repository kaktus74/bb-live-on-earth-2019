from datetime import datetime
import os
from os.path import split
from os.path import isdir
import os.path as p
from picamera import PiCamera
import time
from sense_hat import SenseHat
import logging
import logzero
from logzero import logger

sh = SenseHat()
# Czujniki
        
start = datetime.now()
# Czas startu

nazwa = 'ISS (ZARYA)'
line1='1 25544U 98067A   04236.56031392  .00020137  00000-0  16538-3 0  9993'
line2='2 25544  51.6335 344.7760 0007976 126.2523 325.9359 15.70406856328906'
# Dane do obliczenia pozycji

dir_path = p.dirname(p.realpath(__file__))
# Tworzenie pliku z data

czas_trwania = datetime.now() - start
while czas_trwania.total_seconds() < 10800:
	print('Obliczam pozycje i zapisuje razem ze zdjeciem')
	time.sleep(1)
	logzero.logfile(dir_path+"/wektor_magnetyczny_x_y_z.scv")
	raw = sh.get_compass_raw()
	logger.info(raw)
	time.sleep(1)
	czas_trwania = datetime.now() - start

