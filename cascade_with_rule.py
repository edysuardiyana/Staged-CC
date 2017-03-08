import csv
from collections import namedtuple
import feature_extract
import operator
import source_var
import timeit


THRESHOLD_VALUE = 1.6
ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC ANNOT'
                             ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOTTHIGH') ##with micro annotation

#ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
#                             ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')



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


def find_max(vect_array):
    """ This functions is used to find the highest peak """
    vector_temp=[]
    for line in vect_array:
        vector_temp.append(line.AVMC)
    index, max_val = max(enumerate(vector_temp),key=operator.itemgetter(1))
    micro_annot  = vect_array[index].ANNOT
    return index,max_val,micro_annot

def rule_2_implementation(vect_array,max_value):
    """This function is used to validate rule 2: make sure that max_value is the highest value within vect_array"""
    counter_index = 0
    maximum_flag = True
    while counter_index < len(vect_array) and maximum_flag:
        if vect_array[counter_index].AVMC > max_value:
            maximum_flag = False
        counter_index = counter_index + 1
    return maximum_flag


def simulate_cascade(chest_array,freq_rate, features_path, runtime_path):
    """ This functions simulates the cascade classifier by reading the sample one by one """
    impact_flag = False
    post_flag = False
    max_index = 0
    micro_annot = 0
    max_value = 0
    general_buffer = []
    buffer_test = []
    run_time_array = []

    for line in chest_array:
        general_buffer.append(line)

        if not impact_flag :
            general_buffer, impact_flag, max_value, max_index, micro_annot, pre_runtime =  pre_impact_phase(general_buffer, freq_rate,
            max_value, max_index, micro_annot)
            if pre_runtime > 0:
                run_time_array.append([pre_runtime,0,0])

        else:
            if not post_flag:
                general_buffer, post_flag, impact_flag, imp_runtime = impact_phase(general_buffer,
                max_index, max_value, freq_rate)
                if imp_runtime > 0:
                    run_time_array.append([0,imp_runtime,0])
            else:
                general_buffer, impact_flag, post_flag, max_value, max_index, buffer_test, post_runtime = post_impact(general_buffer,
                max_index, features_path,runtime_path, micro_annot, freq_rate, max_value, buffer_test)
                if post_runtime > 0:
                    run_time_array.append([0,0,post_runtime])

    write_runtime(run_time_array, runtime_path)
    del run_time_array[:]

    return buffer_test


def pre_impact_phase(general_buffer, freq_rate, max_value, max_index, micro_annot):
    """ identify if there was a peak value greater than the threshold in the 1-3 second part of the window
        *** State_1 ****
    """
    impact_flag = False
    buffer_size = freq_rate
    active_win_len = freq_rate * 3
    active_win_init = freq_rate * 2
    run_time = 0

    if len(general_buffer) >= active_win_len:
        #calculate active state

        start_time = timeit.default_timer()
        max_in, max_value, micro_annot = find_max(general_buffer[buffer_size:active_win_len])
        max_index = max_in + buffer_size
        if max_value > THRESHOLD_VALUE: # an active state detected
            impact_flag = True # start collecting impact and post impact values
        else: #no active_state
            del general_buffer[0:active_win_init] #slide window and left 1 sec for buffer
        end_time = timeit.default_timer()
        run_time = end_time - start_time

    return general_buffer, impact_flag, max_value, max_index, micro_annot, run_time


def impact_phase(general_buffer, max_index, max_value, freq_rate):
    """ identify if the active sample is the highest peak
        *** State_2 ****
    """
    impact_flag = True
    post_flag = False
    buffer_size = freq_rate
    seg_win = freq_rate * 2
    active_win_init = freq_rate * 2
    run_time = 0
    if len(general_buffer)>= (max_index+seg_win): #check for the second rule
        #_, max_value2,_ = find_max(general_buffer[max_index-buffer_size:max_index+seg_win])
        #if max_value2 == max_value  :
        start_time = timeit.default_timer()
        if rule_2_implementation(general_buffer[max_index-buffer_size:max_index+seg_win],max_value):
            post_flag = True
        else:
            del general_buffer[0:active_win_init]
            impact_flag = False

        end_time = timeit.default_timer()
        run_time = end_time - start_time

    return general_buffer, post_flag, impact_flag, run_time


def post_impact(general_buffer, max_index, features_path, runtime_path, micro_annot, freq_rate, max_value, buffer_test):
    """ This function is used to call feature extraction process when the length of the general buffer is equal
        to max_index + 1 + 4 seconds window
        *** State_3 ****
    """
    impact_flag = True
    post_flag = True
    buffer_size = freq_rate
    post_win = freq_rate * 4
    active_win_init = freq_rate * 2
    run_time = 0

    if len(general_buffer) >= (max_index + post_win):
        out_file = open(features_path, "a")
        csv_writer = csv.writer(out_file, delimiter='\t')

        start_time = timeit.default_timer() #start the timer for feature calculation
        instance = feature_extract.calc_features(general_buffer[max_index - buffer_size : (max_index + post_win)],micro_annot, freq_rate)
        end_time = timeit.default_timer() #end the timer for feature calculation

        run_time = end_time-start_time

        buffer_test = (test_print(general_buffer[max_index - buffer_size : (max_index + buffer_size + post_win)], buffer_test)) # for testing
        del general_buffer[0:active_win_init] #slide the window for the next two second and left 1 second data as a buffer
        impact_flag = False
        post_flag = False
        max_value = 0
        max_index = 0
        csv_writer.writerow(instance)
        out_file.close()

    return general_buffer, impact_flag, post_flag, max_value, max_index,buffer_test, run_time

def write_runtime(runtime, runtime_path):
    """This function is used to write the runtime into a file"""
    outfile = open(runtime_path,"w")
    csv_writer = csv.writer(outfile)
    for elem in runtime:
        csv_writer.writerow(elem)
    outfile.close


def test_print(data_array, buffer_test):
    """ This function is used to generate output for test case """
    #outF = open("/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/test.csv", "a")
    #csvWriter = csv.writer(outF, delimiter='\t')
    for i in range(len(data_array)):
        #csvWriter.writerow(data_array[i])
        buffer_test.append(data_array[i])
    #print "writing a test case is done"
    return buffer_test


def run_cascade(freq_rate,path,features_path, runtime_path):
    chest_array = read_data(path)
    buffer_test = simulate_cascade(chest_array, freq_rate, features_path, runtime_path)

    return buffer_test

#def main():
    #source_path = '/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/test_cases_rule/double_peak_first_peak_source.csv'
    #features_path = '/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/features_dummy/feat.csv'
    #definition()
    #chest_array = read_data(source_path)
    #simulate_cascade(chest_array, 100, features_path)

    #cascade_funct(100, chest_array,"/Users/ArseneLupin/Documents/edy/experiment_new_cascade/test/features_dummy/feat.csv")

#if __name__ == '__main__':
    #definition()
    #main()
