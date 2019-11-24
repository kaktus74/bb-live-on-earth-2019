import ephem
import time
nazwa='iss'
linijka1='1 25544U 98067A   19328.47806978  .00001893  00000-0  41124-4 0  9999'
linijka2='2 25544  51.6463 286.5827 0006227 320.1499 141.5168 15.50037910200122'
iss=ephem.readtle(nazwa,linijka1,linijka2)
while True:
    iss.compute()
    print(iss.sublat, iss.sublong)
    time.sleep(1)
