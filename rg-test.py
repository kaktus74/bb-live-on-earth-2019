from datetime import datetime, timezone
import time
from ephem import readtle, degree
import reverse_geocoder as rg
name = 'ISS (ZARYA)'
line1='1 25544U 98067A   20033.25120128  .00002314  00000-0  49941-4 0  9990'
line2='2 25544  51.6428 301.0629 0005407 220.6572 248.5738 15.49135306210949'
iss = readtle(name, line1, line2)
t = datetime.now(timezone.utc)
iss.compute(t)
pos = (iss.sublat/degree, iss.sublong/degree)
while True:
    location = rg.search(pos, mode=1)
    print(location)
    
