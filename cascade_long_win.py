import csv
from collections import namedtuple
#import featurescom
import feature_extract
import operator
import numpy as np

THRESHOLD_VALUE = 1.6
ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC ANNOTCHEST'
                             ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOTTHIGH')

#the first rule: the highest peak must be in the impact stage
#the second rule: the act sample must be align with the highest peak from pre-impact and impact stage
def read_data(file_path):
    """ This functions read samples from file """
    chest_data_list = []

    with open(file_path) as raw_data:
        for line in raw_data:
            chest_raw_data = line.split()
            chest_float_data = [float(i) for i in chest_raw_data]
            chest_named_data = ARRAY_TUPLED(*chest_float_data)
            chest_data_list.append(chest_named_data)
        return chest_data_list



def simulate_cascade(chest_array,freq_rate, features_path):

    wind_size = freq_rate * 7
    buffer_size = freq_rate
    active_win = freq_rate * 2
    general_buffer = []
    feature_flag = False
    act_sample = None

    haha = []

    for line in chest_array:
        general_buffer.append(line)
        if not feature_flag:
            #do peaks investigation
            if len(general_buffer) >= wind_size:
                haha, act_sample = check_peak(general_buffer,freq_rate)

                if act_sample is None:
                    del general_buffer[0:active_win]
                else:
                    print "get in"
                    print general_buffer[act_sample].AVMC
                    for k in haha:
                        if general_buffer[k].ANNOTCHEST == 2:
                            print general_buffer[k].AVMC

                    feature_flag = True
        else:
            #do feature extraction
            #print act_sample
            #print general_buffer[act_sample]
            #print general_buffer[act_sample].ANNOTCHEST
            call_feature_extract(general_buffer[act_sample-100:act_sample+400],general_buffer[act_sample].ANNOTCHEST, freq_rate, features_path)
            del general_buffer[0:act_sample+100]
            feature_flag = False

    return len(general_buffer)


def check_peak(general_buffer,freq_rate):

    vm_array = []
    for line in general_buffer:
        vm_array.append(line.AVMC)
    act_sample = find_active_sample(vm_array, freq_rate)
    return act_sample


def find_active_sample(vm_array, freq_rate):

    buffer_win = freq_rate
    active_win = freq_rate * 2
    pre_imp_win = freq_rate * 3

    vm = np.array(vm_array)
    peaks = np.argwhere(vm > 1.6)

    active_peak = None
    temp = None
    for i in range(len(peaks)):
        #not in buffer
        if peaks[i][0]>=buffer_win:
            #not in edge
            if peaks[i] < pre_imp_win:
                #inside 2 secs window
                if temp is None:
                    temp = peaks[i][0]
                if i > 0:
                    if peaks[i] - active_win < peaks[i-1]:
                        if vm[peaks[i-1]] >= vm[peaks[i]]:
                            temp = peaks[i-1][0]
                        else:
                            temp = peaks[i][0]
                    else:
                        active_peak = temp
                        temp = None

    if temp is not None:
        active_peak = temp

    return peaks, active_peak


def call_feature_extract(samples_array,micro_annot,freq_rate, features_path):
    out_file = open(features_path, "a")
    csv_writer = csv.writer(out_file, delimiter='\t')
    instance = feature_extract.calc_features(samples_array,micro_annot,freq_rate)
    #print instance
    csv_writer.writerow(instance)
    out_file.close()


def run_cascade(freq_rate,path,features_path):
    chest_array = read_data(path)
    buffer_test = simulate_cascade(chest_array, freq_rate, features_path)

    return buffer_test

def main():
    freq_rate = 100 #sampling freq_rate
    zeros = ARRAY_TUPLED(*([0.] * 18))

    general_buffer = [zeros] * 113450

    general_buffer[200] = zeros._replace(AVMC=3.,
                                         ANNOTCHEST=2)
    general_buffer[201] = zeros._replace(AVMC=1.7,
                                         ANNOTCHEST=2)
    hoho = simulate_cascade(general_buffer,100,"")
    print hoho
    #source_path = '/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/test_cases_rule/double_peak_first_peak_source.csv'
    #features_path = '/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/features_dummy/feat.csv'
    #definition()
    #chest_array = read_data(source_path)
    #simulate_cascade(chest_array, 100, features_path)

    #cascade_funct(100, chest_array,"/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/features_dummy/feat.csv")

if __name__ == '__main__':
    #definition()
    main()
