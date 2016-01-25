__author__ = 'edy'

import trainingSetGenerator
import source_var

def generate_training():
    list_name = []
    listTrain = []

    with open(source_var.source_var()) as objList:
        for line in objList:
            temp = line.split()
            trainName = temp[0]
            list_name.append(trainName)

    for trainingname in list_name:
        print ("Writing test set for " + trainingname)

        for tempName in list_name:

            if tempName != trainingname:
                listTrain.append(tempName)

        sourcePathTraining = source_var.source_path_training(trainingname)
        wekatrainingDest = source_var.source_path_trainingWeka(trainingname)
        trainingSetGenerator.trainingGenerator(listTrain, sourcePathTraining, wekatrainingDest)
        listTrain = []

    print 'Finish writing training set'

#if __name__ == '__main__':
#    main()
