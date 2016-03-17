from sklearn import tree
import source_var

def main():

    training_path = source_var.source_path_training("bimo")
    target_path = source_var.source_path_features("bimo")

    training_seq_ft = []
    training_class = []
    testing_seq = []
    testing_class = []
    with open(training_path) as tr_obj:
        for line in tr_obj:
            raw_data = line.split()
            training_seq_ft.append(raw_data[:len(raw_data)-1])
            training_class.append(raw_data[len(raw_data)-1])

    with open(testing_path) as test_obj:
        for line_2 in test_obj:
            raw_test = line_2.split
            testing_seq.append(raw_test[:len(raw_test)-1])
            testing_class.append(raw_test[len(raw_test)-1])


    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(training_seq_ft,training_class)
if __name__ == '__main__':
    main()
