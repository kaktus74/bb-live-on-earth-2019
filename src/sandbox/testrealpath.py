import logging
import logzero
from logzero import logger
from sense_hat import SenseHat
import os
import os.path as p

dir_path = p.dirname(p.realpath(__file__))
logzero.logfile(dir_path+"/data01.csv")
logger.info('info')
