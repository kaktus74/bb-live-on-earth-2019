from picamera import PiCamera
import time
cam =  PiCamera()
cam.start_preview()

time.sleep(8)
cam.capture('selfie.jpg')
cam.stop_preview()
