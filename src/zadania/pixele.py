import sense_hat
from time import sleep
# Petla sprawdzajaca wilgotnosc wokol rassbery

okienko = sense_hat.SenseHat()
while True:
    print(okienko.get_humidity())
    sleep(2)
    
    
