__author__ = 'ArseneLupin'

import scale_file
import microannotate_right
import weka_file
import source_var
import cascade_with_rule
import cascade_long_win
import mainTrainingGenerator
import non_cascade
import modify_annot
import activefeat
import training_testing as tt
import csv

def main():
    list_name = read_subject_name(source_var.source_var())
    #cutting_index_list = read_cutting_index(source_var.source_index())
    #print cutting_index_list
    for i in range(len(list_name)):
        name = list_name[i]
        #indexes = cutting_index_list[i]
        print "Processing data from :"
        print name

        source_raw_data = source_var.source_path_data(name)
        source_file_micro = source_var.source_path_scaled(name)
        freq_rate = source_var.sampling_rate()
        micro_path = source_var.source_path_micro(name)
        features_path = source_var.source_path_features(name)
        source_weka = source_var.source_path_wekafile(name)
        source_runtime = source_var.source_runtime(name)
        active_source = source_var.source_path_active(name)

        #scale_file.scale_file(source_raw_data, source_file_micro, indexes[0], indexes[1])
        microannotate_right.micro_annotate(source_file_micro, micro_path) #re-annotate using micro-annotation
        activefeat.active_feat(name)
        non_cascade.run_feat_calc(name, freq_rate,active_source ,features_path) # damn you function! yes this is the cascade function

    for j in range(4):
        result = tt.train_test(j)
        write_result(result, j)

def write_result(result, j):

    path = source_var.source_result(j)

    list_result = []
    header = ["Name","TP","FP","TN", "FN", "Prec","Rec","FScore", "Spec"]
    list_result.append(header)

    for line in result:
        list_result.append(line)

    out_file = open(path, "w")
    csv_writer = csv.writer(out_file, delimiter='\t')

    for raw in list_result:
        csv_writer.writerow(raw)

    out_file.close()

def read_subject_name(source_path):
    name_list = []
    with open(source_path) as list_obj:
        for line in list_obj:
            sub_name = line.split()
            name_list.append(sub_name[0])
    return name_list

def read_cutting_index(source_path):
    index_list = []
    new_indexes = []
    with open(source_path) as list_obj:
        for line in list_obj:
            indexes = line.split(",")
            new_indexes = [float(x) for x in indexes[:len(indexes)]]
            index_list.append(new_indexes)
    print index_list
    return index_list

if __name__ == '__main__':
    main()



#old pieces of code
#weka_file.write_weka(features_path, source_weka) # create the weka file
#mainTrainingGenerator.generate_training()
