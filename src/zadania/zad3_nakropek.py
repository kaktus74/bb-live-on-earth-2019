import ephem
import time
from datetime import datetime, timezone
import os
import os.path
from os.path import split
from os.path import isdir
import sys

#my_dir = split (__file__) [0]
#data_dir = '{0}/../../data/'.format (my_dir)
#t = datetime.now(timezone.utc)

#if isdir (data_dir) == False:
   # print ('Nie znaleziono folderu {0}. Zamierzam go stworzyć.'.format (data_dir))
  #  os.mkdir (data_dir)
#else:
 #   print ('Trwa zapisywanie pliku w folderze {0}'.format (data_dir))

#sys.stdout.flush()

#nazwa = 'ISS (ZARYA)'

#linijka1='1 25544U 98067A   19328.47806978  .00001893  00000-0  41124-4 0  9999'
#linijka2='2 25544  51.6463 286.5827 0006227 320.1499 141.5168 15.50037910200122'

#ISS_pozycje = open ('{0}/../../data/ISS_pozycje_{1}.txt'.format(my_dir, t.strftime("%d-%m-%Y-%H-%M")), 'w')

#iss=ephem.readtle(nazwa,linijka1,linijka2)

#mytime = 0

#while mytime < 10:
 #   ISS_pozycje.write (str (t))
  #  iss.compute(t)
   # ISS_pozycje.write (("{2} {0} {1}/n".format(iss.sublat, iss.sublong, t.strftime("%d-%m-%Y %H:%M:%S"))))
  #time.sleep(5)
  #  mytime = mytime + 5/60


my_dir = split (__file__)
my_dir = list (my_dir [:-1])
my_dir = '/'.join ([str (i) for i in my_dir])
print (__file__)
f = open ('{0}/magnetic_field.txt'.format (my_dir), 'w+')
