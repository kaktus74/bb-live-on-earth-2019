import ephem
import time
from datetime import datetime, timezone

nazwa='ISS (ZARYA)'

################################################################################
# Opis formatu TLE (ang):
# https://www.space-track.org/documentation#/tle

#TLE z NORAD (http://www.celestrak.com/NORAD/elements/stations.txt)
linijka1='1 25544U 98067A   19328.47806978  .00001893  00000-0  41124-4 0  9999'
linijka2='2 25544  51.6463 286.5827 0006227 320.1499 141.5168 15.50037910200122'


#TLE z space-track.org
#linijka1='1 25544U 98067A   19328.79613500  .00002724  00000-0  55632-4 0  9994'
#linijka2='2 25544  51.6462 285.0063 0006257 321.3815 116.3095 15.50041468200172'
          
def angle2exifLonRef(issLonAngle):
    issLonstr = str(issLonAngle).split(':')
    issLonAngle2 = [float(z) for z in issLonstr]
    if issLonAngle2 [0] < 0:
        return 'W'
    else:
        return 'E'
        
    
#def angle2exif(issAngle):
    #return '23/1 45/1 3213/10'

#                      'S' (exif:GPSLatitudeRef)
#                     /
# iss lat str(iss.sublat) = '-45:34:12.1' -> split -> [,,]
#                    \
#                     '45/1 34/1 121/10' (exif:GPSLatitude)


iss=ephem.readtle(nazwa,linijka1,linijka2)
while True:
    t = datetime.now(timezone.utc)
    print(t)
    iss.compute(t)
    
    print("Original values: {2} {0} {1}".format(iss.sublat, iss.sublong, t.strftime("%d-%m-%Y %H:%M:%S")))
    print("EXIF values: E or W? {0}".format(angle2exifLonRef(iss.sublong)))
    
    print(str(iss.sublat))
    
    time.sleep(1)




