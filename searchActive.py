__author__ = 'edy'

import source_var
import numpy
import operator

THRESHOLD_ACCEL = 1.6
ACTIVE_STATE = 1
NON_ACTIVE_STATE = 0
def searchactive(datarray):

    samp_rate = source_var.sampling_rate()
    window_size = 2 * samp_rate
    finalarray=[]
    flag = False
    tempArray=[]
    tempcalcArray=[]
    ind=0

    while flag == False:
        if (ind + window_size) <= len(datarray):
            endIndex = ind + window_size
            tempArray = datarray[ind:endIndex]
            tempcalcArray = activeFeat(tempArray)

        else:
            tempArray = datarray[ind : len(datarray)]
            tempcalcArray = activeFeat(tempArray)
            flag = True

        ind = ind + window_size

        for x in range(len(tempcalcArray)):
            finalarray.append(tempcalcArray[x])

        tempArray = []
        tempcalcArray=[]

    return finalarray

def activeFeat(valArray):


    maxIndex = 0
    newData=[]

    initValue = valArray[0]
    maxVal = initValue[6]

    maxIndex = find_max(valArray)

    for j in range(len(valArray)):
        tempdatdat = valArray[j]
        if j == maxIndex:
            if tempdatdat[6] > THRESHOLD_ACCEL:
                tempdatdat.append(ACTIVE_STATE)
            else:
                tempdatdat.append(NON_ACTIVE_STATE)
        else:
            tempdatdat.append(NON_ACTIVE_STATE)
        newData.append(tempdatdat)
    return newData

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

def find_max_index(data_array):

    #n_array = numpy.array(data_array)
    #x = n_array.argmax(axis=0)

    index, value = max(enumerate(data_array), key= operator.itemgetter(1))

    return index #x[len(x)-1]
