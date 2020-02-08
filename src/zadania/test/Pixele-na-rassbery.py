
import sense_hat
from time import sleep
okienko = sense_hat.SenseHat()
okienko.clear()
for x in range(0,8):
	okienko.set_pixel(x,x,134,58,200)
	okienko.set_pixel(7-x,0+x,134,58,200)
	sleep(1)

okienko.clear()
