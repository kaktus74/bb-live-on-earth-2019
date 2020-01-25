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
def angle2exifLon(issLon):
    isssublong = str(issLon).split(':')
    isssublong2 = [float(i) for i in isssublong]
    #isssublong2 //nie umiem//
    


def angle2exifLatRef(x):
    issLatstr = str(issLatAngle).split(':')
    issLatAngle2 = [float(z) for z in issLatstr]
    if issLatAngle2 [0] < 0:
        return 'S'
    else:
        return 'N'

        
# '-47:45:43.5' <--------- ptzykładowy angle
#int = liczba całkowita np. 2 3 4 154623 ,,, float = liczba z przecinkiem i coś po nim lub nie czyli w pythonie to np. 1.0 2.4 52637.2 5127.1
#jeżeli liczbę całlkowitą na float to mamy np. 1.0   ,    457689.0
#def angle2exif(issAngle):
    #return '23/1 45/1 3213/10'
#                      'S' (exif:GPSLatitudeRef)
#                     /
# iss lat str(iss.sublat) = '-45:34:12.1' -> split -> ['-45','34','12.1'] -> for -> [-45,34, 12.1] -> format -> '45/1 34/1 121/10'
#                    \
#                     '45/1 34/1 121/10' (exif:GPSLatitude)
# lat - szerokosc S(-)/N - > ... jak niżej ale Lat
# lon - dlugosc E/W(-) -> 'GPS.GPSLongitude' ('45/1 34/1 121/10') oraz 'GPS.GPSLongitudeRef' (E/W)



iss=ephem.readtle(nazwa,linijka1,linijka2)
while True:
    t = datetime.now(timezone.utc)
    print(t)
    iss.compute(t)
    print(iss)
    #print(type(iss.sublong)) #Angle
    print(iss.sublong) #sublat
    lonRef = angle2exifLonRef(issLonAngle=iss.sublong)
    lon = angle2exifLon(iss.sublong)
    #print("Original values: {2} {0} {1}".format(iss.sublat, iss.sublong, t.strftime("%d-%m-%Y %H:%M:%S")))
    print("EXIF values: E or W? {0}".format(lonRef))
    print(iss.sublat)
    latRef = angle2exifLatRef(iss.sublat)
    print("EXIF values: N or S? {0}".format(latRef))
    time.sleep(1)



