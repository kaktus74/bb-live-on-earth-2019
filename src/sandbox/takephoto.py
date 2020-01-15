from picamera import PiCamera
from datetime import datetime
import time

cam =  PiCamera()

cam.start_preview()
while True:
    fname = '{0}-chodkiewicza.jpg'.format(datetime.now())
    print('Robię zdjęcie...')
    cam.capture(fname)
    print('Zdjęcie zapisane w pliku {0}'.format(fname))
    time.sleep(30)
    
cam.stop_preview()
