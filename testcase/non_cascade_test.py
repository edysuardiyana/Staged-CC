import unittest
import csv
import os
import non_cascade
from non_cascade import ARRAY_TUPLED,feat_extract

source_dir = os.path.dirname(os.path.realpath(__file__))

class non_cascade_test(unittest.TestCase):
    def non_cascade_test_1(self):

        print source_dir
        features_path = os.path.join(source_dir, 'test_cases_rule/feature_path/feature_test.csv')

        zeros = ARRAY_TUPLED(*([0.]*18))
        general_buffer = [zeros]*1000
        freq_rate = 100
        counter = non_cascade.feat_extract(general_buffer,freq_rate,features_path)

        self.assertEqual(counter,500)

if __name__ == '__main__':
    unittest.main()
