__author__ = 'ArseneLupin'

#This program scales the gyro's raw data

SENSE_DIV = 2.731

def gscale( rawdata, reffval):

    val = (rawdata-reffval)/float(SENSE_DIV)

    return val
