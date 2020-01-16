from picamera import PiCamera
from datetime import datetime
import time
import os.path as p
dirpath = p.dirname(p.realpath(__file__))
cam =  PiCamera()
cam.start_preview()

while True:
    filenamex = 'zdjęcie_sernika.png'
    cam.capture(dirpath + filenamex)
    print('Zdjęcie zapisane w pliku {0}'.format(filenamex))
    time.sleep (10)



cam.stop_preview()
