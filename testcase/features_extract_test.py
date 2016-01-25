import unittest
import feature_extract
import csv
import os

source_dir = os.path.dirname(os.path.realpath(__file__))

class feature_extract_test(unittest.TestCase):
    def feature_extraction_test(self):
        """feature_extraction_test = this tests checks the result of feature calculation"""

        source_path = os.path.join(source_dir, 'cascade_test/features_extract.csv')
        result_path = os.path.join(source_dir, 'cascade_test/feat_result.csv')
        array = []

        array_target = []

        freq_rate = 100 #sampling freq_rate
        micanot = 2

        with open(source_path) as raw_source:
            for line in raw_source:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                array.append(raw_data_final)

        with open(result_path) as raw_target:
            for feat_line in raw_target:
                target_data = feat_line.split()
                target_data_final = [float(i) for i in target_data]

        result_list = feature_extract.calc_features(array,micanot,freq_rate)
        for i in range(len(result_list)):
            self.assertEqual(target_data_final[i],result_list[i])

if __name__ == '__main__':
    unittest.main()
