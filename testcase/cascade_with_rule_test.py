import unittest
import cascade_with_rule
import csv
import os

source_dir = os.path.dirname(os.path.realpath(__file__))

class cascade_rule_test(unittest.TestCase):
    def first_high_peak_test(self):

        """first_high_peak_test: there is a high peak before the highest peak"""

        source_path = os.path.join(source_dir, 'test_cases_rule/double_peak_first_peak_source.csv')
        target_path = os.path.join(source_dir, 'test_cases_rule/double_peak_first_peak.csv')
        feature_path = os.path.join(source_dir, 'test_cases_rule/feature_path/double_peak_first_peak.csv')
        runtime_path = os.path.join(source_dir, 'test_cases_rule/runtime/double_peak_first_peak.csv')


        freq_rate = 100 #sampling freq_rate

        result_list = cascade_with_rule.run_cascade(freq_rate, source_path, feature_path,runtime_path)

        target_list = []

        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])


    #one peak in second segment
    def second_high_peak_test(self):

        """second_high_peak_test = there is a high peak after the highest peak"""

        source_path = os.path.join(source_dir, 'test_cases_rule/double_peak_second_peak_source.csv')
        target_path = os.path.join(source_dir, 'test_cases_rule/double_peak_second_peak.csv')
        feature_path = os.path.join(source_dir, 'test_cases_rule/feature_path/double_peak_second_peak.csv')
        runtime_path = os.path.join(source_dir, 'test_cases_rule/runtime/double_peak_first_peak.csv')


        freq_rate = 100 #sampling freq_rate
        result_list = cascade_with_rule.run_cascade(freq_rate, source_path, feature_path,runtime_path)
        target_list = []

        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])


    #similar segment
    def normal_segment_test(self):

        """normal_segment: for ideal segment"""
        source_path = os.path.join(source_dir, 'test_cases_rule/normal_segment_source.csv')
        target_path = os.path.join(source_dir, 'test_cases_rule/normal_segment.csv')
        feature_path = os.path.join(source_dir, 'test_cases_rule/feature_path/normal_segment.csv')
        runtime_path = os.path.join(source_dir, 'test_cases_rule/runtime/double_peak_first_peak.csv')


        freq_rate = 100 #sampling freq_rate
        result_list = cascade_with_rule.run_cascade(freq_rate, source_path, feature_path,runtime_path)
        target_list = []

        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])


if __name__ == '__main__':
    unittest.main()
