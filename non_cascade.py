from collections import namedtuple
import feature_extract

ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC ANNOTCHEST'
                             ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOTTHIGH')

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

def feat_extract(chest_array,freq_rate, features_path):
    #this function is for doing the feaqture extraction
    start_index = freq_rate
    end_index = freq_rate * 4
    out_file = open(features_path, "a")
    csv_writer = csv.writer(out_file, delimiter='\t')
    counter = 0
    for i in range(start_index, len(chest_array) - end_index):
        features_value = feature_extract.calc_features(chest_array[i-freq_rate:i+end_index],chest_array[i].ANNOTCHEST,freq_rate)
        csv_writer.writerow(features_value)
        counter = counter + 1
    out_file.close()
    return counter

def run_feat_calc(freq_rate,path,features_path):
    #main caller for feature extraction
    chest_array = read_data(path)
    buffer_test = feat_extract(chest_array, freq_rate, features_path)

    return buffer_test
