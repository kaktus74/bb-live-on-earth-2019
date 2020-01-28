import ephem
import time
from datetime import datetime, timezone

nazwa='ISS (ZARYA)'

################################################################################
# Opis formatu TLE (ang):
# https://www.space-track.org/documentation#/tle

#TLE z NORAD (http://www.celestrak.com/NORAD/elements/stations.txt)


linijka1='1 25544U 98067A   20026.35371815 -.00020245  00000-0 -35864-3 0  9997'
linijka2='2 25544  51.6435 335.1909 0005604 194.1990 303.5861 15.49108748209873'




#TLE z space-track.org
#linijka1='1 25544U 98067A   19328.79613500  .00002724  00000-0  55632-4 0  9994'
#linijka2='2 25544  51.6462 285.0063 0006257 321.3815 116.3095 15.50041468200172'

def na_ulamki(x):
    x [0] = abs (x[0])
    x = [str(i) for i in x]
    x [0] += '/1'
    x [1] += '/1'
    x [2] += '/10'
    napis = x[0] + ' ' + x[1] + ' ' + x[2]
    return napis

          
def angle2exifRef(issAngle, directions):
    issLonstr = str(issAngle).split(':')
    issLonAngle2 = [float(z) for z in issLonstr]
    if issLonAngle2 [0] < 0:
        return directions [0]
    else:
        return directions [1]


def angle2exif(issLon):
    isssublong = str(issLon).split(':')
    isssublong = [float(i) for i in isssublong]
    return na_ulamki (isssublong)
    
# zakladamy ze stopnie i minuty sa zawsze calkowite
# issLon, np. '14:45:12.4' -> '14/1 45/1 124/10'

##def angle2exifLatRef(x):
##    issLatstr = str(issLatAngle).split(':')
##    issLatAngle2 = [float(z) for z in issLatstr]
##    if issLatAngle2 [0] < 0:
##        return 'S'
##    else:
##        return 'N'

#mapowanie/mapping
# tab 1  operacja  tab 2
# x       * 2       x2
# [0] 1       * 2    ->   2
# [1] 2       * 2    ->   4
# [2] 3       * 2    ->   6 

        
# '-47:45:43.5' <--------- ptzykładowy angle
#int = liczba całkowita np. 2 3 4 154623 ,,, float = liczba z przecinkiem i coś po nim lub nie czyli w pythonie to np. 1.0 2.4 52637.2 5127.1
#jeżeli liczbę całlkowitą na float to mamy np. 1.0   ,    457689.0
#def angle2exif(issAngle):
    #return '23/1 45/1 3213/10'
#                      'S' (exif:GPS.GPSLatitudeRef)
#                     /
# iss lat str(iss.sublat) = '-45:34:12.1' -> split -> ['-45','34','12.1'] -> for -> [-45,34, 12.1] -> format -> '45/1 34/1 121/10'
#                    \
#                     '45/1 34/1 121/10' (exif:GPSLatitude)
# lat - szerokosc S(-)/N - > ... jak niżej ale Lat
# lon - dlugosc E/W(-) -> 'GPS.GPSLongitude' ('45/1 34/1 121/10') oraz 'GPS.GPSLongitudeRef' (E/W)



iss=ephem.readtle(nazwa,linijka1,linijka2)
for i in range(0,10):
    t = datetime.now(timezone.utc)
    print(t)
    iss.compute(t)
    #print(iss)
    #print(type(iss.sublong)) #Angle
    print("{0} of type {1}, and {2} as string ".format(iss.sublong, type(iss.sublong), str(iss.sublong))) #sublat
    
    #
    
    lonRef = angle2exifRef(issAngle=iss.sublong, directions=['W', 'E'])
    lonExif = angle2exif(iss.sublong)
    latRef = angle2exifRef(issAngle=iss.sublat, directions=['S', 'N'])
    latExif = angle2exif(iss.sublat)    
    
    ##print("Original values: {2} {0} {1}".format(iss.sublat, iss.sublong, t.strftime("%d-%m-%Y %H:%M:%S")))
    print("EXIF values: E or W? {0}".format(lonRef))
    print(lonExif)
    print ('EXIF values: N or S? {0}'.format(latRef))
    print (latExif)
    #latRef = angle2exifLatRef(iss.sublat)
    #print("EXIF values: N or S? {0}".format(latRef))
    time.sleep(1)



