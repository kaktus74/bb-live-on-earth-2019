from datetime import datetime, timezone
import os
from os.path import split
from os.path import isdir
from picamera import PiCamera
import time
from ephem import readtle, degree
from sense_hat import SenseHat
import csv
from logzero import logger, logfile
import reverse_geocoder as rg
sense=SenseHat()

def tales (h1, p1, h2 = 408000):
    p2 = p1 * (h2 / h1)
    return p2

def co_ile (pole_widzenia_m, czas_obiegu_s = 5400, obwod_m = 40075000):
    ile_razy = obwod_m / pole_widzenia_m
    co_ile = czas_obiegu_s / ile_razy
    return co_ile

def dl_maly_bok (dlugi_bok, aspekt = 16/9):
    maly_bok = dlugi_bok  / aspekt
    return maly_bok

measured_distance = 0.56
measured_fov = 0.225
interval = co_ile (dl_maly_bok (tales (measured_distance, measured_fov))) / 2

print("Tales {0}, Co ile {1}, dl_maly_bok {2}".format(tales(measured_distance, measured_fov),co_ile(dl_maly_bok (tales (measured_distance, measured_fov))),dl_maly_bok(tales (measured_distance, measured_fov))))
