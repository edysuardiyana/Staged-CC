__author__ = 'ArseneLupin'


import numpy
from collections import namedtuple
import operator

FALLS_INDEX = 2
NON_FALLS_INDEX = 0

def micAn(arraydat):

    datAr = []
    chestData=[]
    waistData=[]
    thighData=[]

    chestAfter=[]
    waistAfter=[]
    thighAfter=[]

    for arr in arraydat:


        chesttemp = [arr.AXC,arr.AYC,arr.AZC,arr.GXC,arr.GYC,arr.GZC,arr.AVMC,arr.GVMC]
        chestData.append(chesttemp)
        thightemp = [arr.AXT, arr.AYT, arr.AZT, arr.GXT, arr.GYT, arr.GZT, arr.AVMT, arr.GVMT]
        thighData.append(thightemp)

    chestAfter = searchmax(chestData)
    thighAfter = searchmax(thighData)


    for x in range (len(arraydat)):

        tempAr = [chestAfter[x], thighAfter[x]]
        datAr.append(tempAr)

    return datAr


def find_max_index(data_array):

    index, value = max(enumerate(data_array), key= operator.itemgetter(1))

    return index

def find_max(data_array):
    maxIndex = 0

    initValue = data_array[0]
    maxVal = initValue[6]

    for i in range(len(data_array)):
        tempVal = data_array[i]

        if tempVal[6] > maxVal:
            maxVal = tempVal[6]
            maxIndex = i

    return maxIndex


def searchmax(datval):

    arrsize = len(datval)
    maxIndex = find_max(datval)
    for i in range(arrsize):

        datdat = datval[i]

        if i == maxIndex:
            datdat.append(FALLS_INDEX)
        else:
            datdat.append(NON_FALLS_INDEX)

        datval.append(datdat)

    return datval
