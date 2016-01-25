__author__ = 'ArseneLupin'

import source_var
import csv
import writeWeka

def trainingGenerator(training,destFile,trainingArff):

    outF = open(destFile, "w")
    csvWriter = csv.writer(outF, delimiter='\t')
    for name in training:

        training_path = source_var.source_features_training(name)

        with open(training_path) as objectFile:
            for line in objectFile:

                datasplit = line.split()
                writeData = map(float,datasplit[:])
                csvWriter.writerow(writeData)

    outF.close()

    #print 'Writing Training Set'

    writeWeka.writeWeka(destFile,trainingArff)




