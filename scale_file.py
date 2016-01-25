__author__ = 'ArseneLupin'

# This is program for scaling and calculate the vector magnitude of the raw data
# Creator -Edy-

import csv
import ascale
import gscale
import math
from collections import namedtuple

CHEST_INDEX = 1
WAIST_INDEX = 2
THIGH_INDEX = 3


REFF_CHEST_GYRO_X = 1827
REFF_CHEST_GYRO_Y = 1829
REFF_CHEST_GYRO_Z = 1865

REFF_WAIST_GYRO_X = 1864
REFF_WAIST_GYRO_Y = 1880
REFF_WAIST_GYRO_Z = 1810

REFF_THIGH_GYRO_X = 1823
REFF_THIGH_GYRO_Y = 1831
REFF_THIGH_GYRO_Z = 1857

REFF_GYRO_SET = [REFF_CHEST_GYRO_X,REFF_CHEST_GYRO_Y,REFF_CHEST_GYRO_Z,REFF_WAIST_GYRO_X,REFF_WAIST_GYRO_Y,REFF_WAIST_GYRO_Z,
                 REFF_THIGH_GYRO_X,REFF_THIGH_GYRO_Y,REFF_THIGH_GYRO_Z]

ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'SENSE_ID1 AXC AYC AZC GXC GYC GZC TIMESTAMP1 SENSE_ID2 AXW AYW AZW GXW GYW GZW TIMESTAMP2'
                                 ' SENSE_ID3 AXT AYT AZT GXT GYT GZT UNUSED1 UNUSED2 UNUSED3 UNUSED4 UNUSED5 UNUSED6 UNUSED7 ANNOT')

def l2norm(x, y, z):

    return math.sqrt(x * x + y * y + z * z)


def scale_row(raw_data):

    data = ARRAY_TUPLED(*[float(x) for x in raw_data])
    #==============================================================
    #Chest Accel Data
    xChestA = ascale.ascale(data.AXC, CHEST_INDEX, 1)
    yChestA = ascale.ascale(data.AYC, CHEST_INDEX, 2)
    zChestA = ascale.ascale(data.AZC, CHEST_INDEX, 3)

    #Chest Gyro Data
    xChestG = gscale.gscale(data.GXC, REFF_GYRO_SET[0])
    yChestG = gscale.gscale(data.GYC, REFF_GYRO_SET[1])
    zChestG = gscale.gscale(data.GZC, REFF_GYRO_SET[2])

    cavm = l2norm(xChestA, yChestA, zChestA)
    cgvm = l2norm(xChestG, yChestG, zChestG)
    #==============================================================

    #Future Work
    #Waist Accel Data
    #xWaistA = ascale.ascale(float(data[9]), WAIST_INDEX, 1)
    #yWaistA = ascale.ascale(float(data[10]), WAIST_INDEX, 2)
    #zWaistA = ascale.ascale(float(data[11]), WAIST_INDEX, 3)

    #Waist Gyro Data
    #xWaistG = gscale.gscale(float(data[12]), REFF_GYRO_SET[3])
    #yWaistG = gscale.gscale(float(data[13]), REFF_GYRO_SET[4])
    #zWaistG = gscale.gscale(float(data[14]), REFF_GYRO_SET[5])

    #wavm = math.sqrt(xWaistA * xWaistA + yWaistA * yWaistA + zWaistA * zWaistA)
    #wgvm = math.sqrt(xWaistG * xWaistG + yWaistG * yWaistG + zWaistG * zWaistG)


    #==============================================================
    #Thigh Accel Data
    xThighA = ascale.ascale(data.AXT, THIGH_INDEX, 1)
    yThighA = ascale.ascale(data.AYT, THIGH_INDEX, 2)
    zThighA = ascale.ascale(data.AZT, THIGH_INDEX, 3)

    #Thigh Gyro Data
    xThighG = gscale.gscale(data.GXT, REFF_GYRO_SET[6])
    yThighG = gscale.gscale(data.GYT, REFF_GYRO_SET[7])
    zThighG = gscale.gscale(data.GZT, REFF_GYRO_SET[8])

    tavm = l2norm(xThighA, yThighA, zThighA)
    tgvm = l2norm(xThighG, yThighG, zThighG)
    #==============================================================

    anDat = data.ANNOT

    outputList = [xChestA, yChestA, zChestA, xChestG, yChestG, zChestG, cavm, cgvm, xThighA, yThighA, zThighA,
                xThighG, yThighG, zThighG, tavm, tgvm, anDat]

    return outputList


    
def scale_file(sourceFile, destFile, initcut, endcut):


    print("This Program is scaling your data now")
    print("Processing ....")

    counter = 0
    start_flag = False
    counter = 0

    data_pool = []
    outF = open(destFile, "w")
    csvWriter = csv.writer(outF, delimiter='\t')


    with open(sourceFile) as open_in_file:
        for line in open_in_file:

            if start_flag is False:
                if counter >= initcut - 1:
                    start_flag = True

            elif counter > endcut:
                    start_flag = False

            if start_flag is True:

                data = line.split()
                
                output_list = scale_row(data)

                csvWriter.writerow(output_list)

            counter += 1

    print("Finish")

    outF.close()


#def process_csv_file(infile, outfile, func, start_row, end_row):
    #outf = open(outfile, "w")
    #csv_writer = csv.writer(outf, delimiter='\t')

    #row_count = 0
    #with open(infile) as open_in_file:
        #for row in csv.reader(open_in_file):
            #if row_count < start_row:
                #continue
            #elif row_count > end_row:
                #break
            #else:
                #out = func(row)
                #csv_writer.writerow(out)
                
