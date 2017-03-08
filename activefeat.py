__author__ = 'ArseneLupin'

#this program is for checking active state

import source_var
import searchActive
import csv

CHEST_WIN = [0, 9]
THIGH_WIN = [9, 18]
#WAIST_WIN = [18, 27]

def active_feat(name):
    sourceFile = source_var.source_path_micro(name)
    destFile = source_var.source_path_active(name)

    chestArray=[]
    thighArray=[]
    waistArray=[]

    finalChestArray=[]
    finalThighArray=[]
    finalWaistArray=[]

    print 'Searching for Active State'

    with open(sourceFile) as objectFile:

        for line in objectFile:

            data = line.split()
            chestData = map(float,data[CHEST_WIN[0]:CHEST_WIN[1]])
            chestArray.append(chestData)

            thighData= map(float,data[THIGH_WIN[0]:THIGH_WIN[1]])
            thighArray.append(thighData)

            #waistData = map(float,data[WAIST_WIN[0]:WAIST_WIN[1]])
            #waistArray.append(waistData)

    finalChestArray = searchActive.searchactive(chestArray)
    finalThighArray = searchActive.searchactive(thighArray)
    #finalWaistArray = searchActive.searchactive(waistArray)

    outF = open(destFile, "w")
    csvWriter = csv.writer(outF, delimiter='\t')

    for i in range(len(finalChestArray)):


        ff1 = finalChestArray[i] #--,,-- chest data
        #ff2 = finalWaistArray[i] #--,,-- thigh data
        ff2 = finalThighArray[i] #--,,-- waist data
        datfinal = ff1 + ff2 #--,,--

        csvWriter.writerow(datfinal)

    outF.close()
