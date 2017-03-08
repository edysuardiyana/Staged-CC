import source_var as src
from sklearn import tree,svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier, LogisticRegressionCV
import csv
import cPickle

FALL_FORWARD = 2
FALL_BACKWARD = 6
FALL_LEFT = 10
FALL_RIGHT = 11
FALL_BLIND_FORWARD = 12
FALL_BLIND_BACKWARD = 13

FALL_SET = set([FALL_FORWARD,
                FALL_BACKWARD,
                FALL_LEFT,
                FALL_RIGHT,
                FALL_BLIND_FORWARD,
                FALL_BLIND_BACKWARD])

def train_test(code_classifier):
    training_set = []
    class_training = []
    annot_training = []
    total_training_set = []
    total_class_training = []

    testing_set = []
    class_testing = []
    annot_testing = []
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    Prec = 0
    Rec = 0
    Fscore = 0
    Spec = 0
    res_sequence = []
    list_name = read_training_testing_file(2)
    if code_classifier == 0:
        clf = svm.SVC()#
        clf_name = "SVM"
    elif code_classifier == 1:
        clf = tree.DecisionTreeClassifier(random_state = 1)
        clf_name = "Decision_Tree"
    elif code_classifier == 2:
        clf = KNeighborsClassifier(n_neighbors = 1, leaf_size = 40)
        clf_name = "KNN"
    else:
        clf = LogisticRegression(C = 1e8)
        clf_name = "Logistic"

    for name in list_name:


        for sub_name in list_name:
            if name == sub_name:
                print "loading test samples"
                testing_set, class_testing = read_file(sub_name)
            else:
                print "loading training samples "+ str(sub_name)
                training_set, class_training = read_file(sub_name)
                for i in range(len(training_set)):
                    total_training_set.append(training_set[i])
                    total_class_training.append(class_training[i])

        print "training and testing " + name
        print len(total_training_set)
        clf = clf.fit(total_training_set, total_class_training)

        prediction_val = clf.predict(testing_set)

        TP, FP, TN, FN = calc_metrics(prediction_val, class_testing, name)
        #the case when the result is on the edge
        if TP == 0 and FP == 0:
            Prec = 0
        else:
            Prec = float(TP)/(TP+FP) * 100
        Rec = float(TP)/(TP + FN) * 100
        Fscore = float((2*TP))/((2*TP)+FP+FN) * 100
        Spec = float(TN)/(FP + TN) * 100
        del total_training_set[:]
        del total_class_training[:]

        result_metric = [name,TP, FP, TN, FN, Prec, Rec, Fscore, Spec]
        res_sequence.append(result_metric)

        #print_read_classifier(fin_ml, clf_name, code, percentage, True)

    return res_sequence

def calc_metrics(prediction_val, class_testing, name):
    TP = 0
    FP = 0
    TN = 0
    FN = 0
    Prec = 0
    Rec = 0
    Fscore = 0
    Spec = 0
    temp_val = []
    temp_annot = 0
    for i in range(len(prediction_val)):

        result = accuracy_check(prediction_val[i], class_testing[i])
        if result == 1:
            TP = TP + 1
        elif result == 2:
            FP = FP + 1
        elif result == 3:
            TN = TN + 1
        else:
            FN = FN + 1

    return TP, FP, TN, FN

def accuracy_check(final_detec_flag, annot):
    result = 0
    if annot == 2 and final_detec_flag == 2:
        #true positive
        result = 1
    elif annot == 0  and final_detec_flag == 2:
        #false positive
        result = 2
    elif annot == 0 and final_detec_flag == 0:
        #true negative
        result = 3
    else: #in Fall Set and not final_detec_flag
        #false negative
        result = 4
    return result


def read_file(name):

    path = src.source_path_features(name)

    data = []
    class_flag = []

    with open(path) as accel:
        for line in accel:
            raw_data = line.split()
            ori_data_pre = [float(i) for i in raw_data[:len(raw_data)]]
            ori_data = [round(k,6) for k in ori_data_pre[:len(ori_data_pre)]]
            feature_data = ori_data[0:len(ori_data)-1]
            #print feature_data
            data.append(feature_data)
            class_flag.append(ori_data[len(ori_data)-1]) #last element
    return data, class_flag

def read_training_testing_file(code): #0 for training and testing , 1 for outsample test, other for normal test
    name_list = []
    if code == 0:
        path = src.training_path()
    elif code == 1:
        path = src.testing_path()
    else:
        path = src.source_var()

    with open(path) as obj:
        for line in obj:
            raw_data = line.split()
            name = raw_data[0]
            name_list.append(name)
    return name_list

def main():
    TP, FP, TN, FN, Prec, Rec, Fscore, Spec = train_test_nonover(["kao","musaab"])
    print TP
    print FP
    print TN
    print FN


if __name__ == '__main__':
    main()
