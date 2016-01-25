__author__ = 'ArseneLupin'

import scale_file
import microannotate_right
import weka_file
import source_var
import cascade_with_rule
import cascade_long_win
import mainTrainingGenerator

def main():
    name_path = source_var.source_var()
    list_name = read_subject_name(name_path)
    for name in list_name:
        print "Extracting features from :"
        print name
        source_file_micro = source_var.source_path_scaled(name)
        freq_rate = source_var.sampling_rate()
        micro_path = source_var.source_path_micro(name)
        features_path = source_var.source_path_features(name)
        source_weka = source_var.source_path_wekafile(name)

        source_runtime = source_var.source_runtime(name)

        microannotate_right.micro_annotate(source_file_micro, micro_path) # re-annotate the raw data using micro-annotate
        cascade_with_rule.run_cascade(freq_rate,micro_path,features_path,source_runtime)
        #cascade_long_win.run_cascade (freq_rate,micro_path,features_path)
        weka_file.write_weka(features_path, source_weka) # create the weka file

    mainTrainingGenerator.generate_training()


def read_subject_name(source_path):
    name_list = []
    with open(source_path) as list_obj:
        for line in list_obj:
            sub_name = line.split()
            name_list.append(sub_name[0])
    return name_list

if __name__ == '__main__':
    main()
