from datetime import datetime
import os
from os.path import split
from os.path import isdir
import os.path as p
from picamera import PiCamera
import time
from time import sleep
from sense_hat import SenseHat
import logging
import logzero
from logzero import logger

sh = SenseHat()
# Czujniki

camera = PiCamera()
camera.resolution = (1296,972)
camera.start_preview()
zmiennadozdjecia = 1
miedzy_zdjeciami = 21.5
# Kamera 
        
start = datetime.now()
# Czas startu

nazwa = 'ISS (ZARYA)'
line1='1 25544U 98067A   04236.56031392  .00020137  00000-0  16538-3 0  9993'
line2='2 25544  51.6335 344.7760 0007976 126.2523 325.9359 15.70406856328906'
# Dane do obliczenia pozycji

dir_path = p.dirname(p.realpath(__file__))
# Tworzenie plików

czas_trwania = datetime.now() - start
while czas_trwania.total_seconds() < 10800:
	print('Obliczam pozycje i zapisuje razem ze zdjeciem')
	camera.capture(dir_path+"/zmiennadozdjecia")
	zmiennadozdjecia = zmiennadozdjecia + 1
	time.sleep(1)
	logzero.logfile(dir_path+"/wektor_magnetyczny_x_y_z.scv")
	raw = sh.get_compass_raw()
	logger.info(raw)
	time.sleep(1)
	czas_trwania = datetime.now() - start
