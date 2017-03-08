__author__ = 'edy'

import ConfigParser

def configParser(section):

    Config = ConfigParser.ConfigParser()
    Config.read('/Users/ArseneLupin/Documents/edy/falls_ver1.3/prop.ini')
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def sampling_rate():
    samp_rate = int(configParser("SectionOne")['sampling_rate'])
    return samp_rate

def source_var():
    name_path = configParser("SectionOne")['source_list_name']
    return name_path

def source_index():
    index_path = configParser("SectionOne")['source_list_index']
    return index_path

def init_val():
    in_val = int(configParser("SectionOne")['initval'])
    return in_val

def end_val():
    en_val = int(configParser("SectionOne")['endval'])
    return en_val

def source_path_data(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_data']
    source_path= path+name+'.txt'
    return source_path

def source_path_scaled(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_scaled']
    scaled_path = path+name+'.csv'
    return scaled_path

def source_path_micro(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_micro']
    micro_path = path+name+'.csv'
    return micro_path

def source_path_active(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_active']
    active_path = path + name +'.csv'
    return active_path

def source_path_features(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_features']
    features_path = path + name + '.csv'
    return features_path

def source_path_wekafile(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_wekafile']
    weka_path = path + name + '.arff'
    return weka_path

def source_path_training(name):
    path = configParser("SectionOne")['source_path_training']
    training_path = path+name+'-training.csv'
    return training_path

def source_path_trainingWeka(name):
    path = configParser("SectionOne")['source_path_training_weka']
    trainingWeka_path = path + name + '-training.arff'
    return trainingWeka_path

def source_features_training(name):
    path = configParser("SectionOne")['source_features_training']
    features_training_path = path + name + '.csv'
    return features_training_path

def source_runtime(name):
    #name = source_var()
    path = configParser("SectionOne")['source_path_runtime']
    runtime = path + name + '.csv'
    return runtime

def source_result(code_classifier):
    if code_classifier == 0:
        clf = "SVM"
    elif code_classifier == 1:
        clf = "DT"
    elif code_classifier == 2:
        clf = "KNN"
    else:
        clf = "LR"
    path = configParser("SectionOne")['source_result']
    result = path+clf+'.csv'
    return result
