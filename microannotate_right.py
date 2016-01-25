__author__ = 'ArseneLupin'

# this program is for re-annotate the falls
# 2, 6, 10, 11, 12, 13 --> fall annotation
# annotation = data[21]

import csv
import searchmax
from collections import deque, namedtuple
import reannotright
import itertools
import source_var


FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])
def micro_annotate_search(sourceFile):

    flag = False
    counter = 0
    tempData = []
    output = []
    quemican = deque
    ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                                 ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')

    print('start to re-annotate')
    with open(sourceFile) as objectFile:
        for line in objectFile:

            dataread = line.split()

            ori_data = [float(x) for x in dataread[:len(dataread)]]
            data = ARRAY_TUPLED(*ori_data)

            if data.ANNOT in FALL_SET: #change this for OJ's data

                tempData.append(data)

                if not flag:
                    flag = True

            elif flag and (data.ANNOT not in FALL_SET) :

                micanDat = searchmax.micAn(tempData) #search for maximum value
                for x in range(len(micanDat)):
                    output.append(micanDat[x])

                flag = False
                tempData = []
                output.append(reannotright.reanotright(data))

            else:

                saveData = reannotright.reanotright(data)
                output.append(saveData)

    #write_csv(destFile, output)
    return output

def micro_annotate(sourceFile, dest_file):

    outF = open(dest_file, "w")
    csvWriter = csv.writer(outF, delimiter='\t')

    output = micro_annotate_search(sourceFile)

    for n in range(len(output)):
        filout = output[n]
        ff1 = filout[0] #chest data
        ff2 = filout[1] #thigh data
        finout = ff1 + ff2
        csvWriter.writerow(finout)

    outF.close()
