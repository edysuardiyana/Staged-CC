__author__ = "ArseneLupin"

import csv

def main():



def combine_fall_dataset():

    trial = 3 #number of trial
    fall_type = ["2","6","10","11"] #fall type, read Readme file to see the type
    source_file = "/Users/ArseneLupin/Documents/edy/experiment_mobifall/data/sub2/"
    dest_file = "/Users/ArseneLupin/Documents/edy/experiment_mobifall/data/sub2/fall.csv"

    temp_array = []

    for i in range(len(trial)):
        index_file  = string(i)
        source1 = source_file + fall_type[1] + i + ".tx"
        source2 = source_file + fall_type[2] + i + ".tx"
        source3 = source_file + fall_type[3] + i + ".tx"
        source4 = source_file + fall_type[4] + i + ".tx"

        with open source1 as object_1:
            for line in object_1:
                splitted_line = line.split(',')
                new_data = splitted_line[1,2,3]








if __name__ = '__main__':
    main()
