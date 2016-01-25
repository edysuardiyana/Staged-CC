import unittest
import cascade_with_rule
from cascade_with_rule import ARRAY_TUPLED
import csv
import os

source_dir = os.path.dirname(os.path.realpath(__file__))

class cascade_rule_impact_test(unittest.TestCase):
    def ideal_test(self):
        """ ideal_test = if there is no double peak issue"""
        source_path = os.path.join(source_dir, 'impact_test/ideal_source.csv')
        target_path = os.path.join(source_dir, 'impact_test/ideal_target.csv')

        target_list = []
        result_list = []
        source_list = []


        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        freq_rate = 100 #sampling freq_rate

        general_buffer = cascade_with_rule.read_data(source_path)
        result_list, post_flag, impact_flag, runtime = cascade_with_rule.impact_phase(general_buffer, 185, 3, freq_rate)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertTrue(impact_flag)
        self.assertTrue(post_flag)

    def ideal_test2(self):
        """ ideal_test = if there is no double peak issue -- using artificial data"""

        freq_rate = 100 #sampling freq_rate
        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[185] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        result_list, post_flag, impact_flag, run_time = cascade_with_rule.impact_phase(general_buffer, 185, 3, freq_rate)

        self.assertEqual(400, len(result_list))

        self.assertTrue(impact_flag)
        self.assertTrue(post_flag)

    def before_highest_test(self):

        """before_highest_test: there is a high peak before the highest peak"""

        source_path = os.path.join(source_dir, 'impact_test/before_highest_source.csv')
        target_path = os.path.join(source_dir, 'impact_test/before_highest_target.csv')

        target_list = []
        result_list = []
        source_list = []


        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        freq_rate = 100 #sampling freq_rate

        general_buffer = cascade_with_rule.read_data(source_path)
        result_list, post_flag, impact_flag, run_time = cascade_with_rule.impact_phase(general_buffer, 185, 2, freq_rate)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertFalse(impact_flag)
        self.assertFalse(post_flag)

    def before_highest_test2(self):
        """before_highest_test: there is a high peak before the highest peak -- using artificial data"""

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[185] = zeros._replace(AVMC=2.,
                                             ANNOTCHEST=0)

        general_buffer[186] = zeros._replace(AVMC=3.5,
                                         ANNOTCHEST=0)
        freq_rate = 100 #sampling freq_rate

        result_list, post_flag, impact_flag, run_time = cascade_with_rule.impact_phase(general_buffer, 185, 2, freq_rate)

        self.assertEqual(200,len(result_list))
        self.assertFalse(impact_flag)
        self.assertFalse(post_flag)


    def after_highest_test(self):

        """after_highest_test= there is a high peak after the highest peak"""

        source_path = os.path.join(source_dir, 'impact_test/after_highest_source.csv')
        target_path = os.path.join(source_dir, 'impact_test/after_highest_target.csv')

        target_list = []
        result_list = []
        source_list = []


        with open(target_path) as raw_target:
            for line in raw_target:
                raw_data = line.split()
                raw_data_final = [float(i) for i in raw_data]
                target_list.append(raw_data_final)

        freq_rate = 100 #sampling freq_rate

        general_buffer = cascade_with_rule.read_data(source_path)
        result_list, post_flag, impact_flag, run_time = cascade_with_rule.impact_phase(general_buffer, 186, 2.5, freq_rate)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertFalse(impact_flag)
        self.assertFalse(post_flag)

    def after_highest_test2(self):
        """after_highest_test= there is a high peak after the highest peak -- Using artificial data"""


        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[185] = zeros._replace(AVMC=3.,
                                         ANNOTCHEST=2)

        general_buffer[186] = zeros._replace(AVMC=2.5,
                                     ANNOTCHEST=0)
        freq_rate = 100 #sampling freq_rate

        result_list, post_flag, impact_flag, run_time = cascade_with_rule.impact_phase(general_buffer, 186, 2.5, freq_rate)

        self.assertEqual(200,len(result_list))
        self.assertFalse(impact_flag)
        self.assertFalse(post_flag)

if __name__ == '__main__':
    unittest.main()
