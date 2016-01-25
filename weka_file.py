__author__ = 'ArseneLupin'

#this program will call the funtion for generating file for weka

import writeWeka
def write_weka(source_features, weka_dest):

    print('The system start to calculate the features ')
    print source_features
    writeWeka.writeWeka(source_features,weka_dest)
    print("Finish")


#old code


#import csv

#import source_var
#import threshold_function
#sourceFile = source_var.source_path_active()
#sourceFeatures = source_var.source_path_features()
#wekadest = source_var.source_path_wekafile()


#chestData =[]
#chestList=[]

#thighData=[]
#thighList=[]

#waistData=[]
#waistList=[]

#chestWeka=[]
#counter = 0
#with open(sourceFile) as objectFile:

    #for line in objectFile:

        #data = line.split()

        #chestData = [float(data[0]),float(data[1]),float(data[2]),float(data[3]),float(data[4]),float(data[5]),float(data[6]),float(data[7]),float(data[8]),float(data[9])]
        #chestList.append(chestData)

        #################################### FUTURE WORK ######################################################
        #thighData = [data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17]]
        #thighList.append(thighData)

        #waistData = [data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25], data[26]]
        #waistList.append(waistData)
        #######################################################################################################

#threshold_function.threshold_function(chestList,sourceFeatures)
