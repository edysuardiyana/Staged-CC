import unittest
from cascade_with_rule import ARRAY_TUPLED
import cascade_with_rule
import csv
import os

source_dir = os.path.dirname(os.path.realpath(__file__))

class cascade_rule_test(unittest.TestCase):
    def no_peak_test(self):

        """ no_peak_test: no peak at all using sample dataset """

        source_path = os.path.join(source_dir, 'pre_impact_test/zero_peak_source.csv')
        target_path = os.path.join(source_dir, 'pre_impact_test/zero_peak_target.csv')

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
        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,1.0438264405)
        self.assertEqual(micro_annot,0)


    def no_peak_test2(self):
        """ no_peak_test2: if accel values all zero, no impact should be flagged."""
        freq_rate = 100 #sampling freq_rate

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        result_list,impact_flag,max_value,_,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(200, len(result_list))

        self.assertFalse(impact_flag)
        self.assertEqual(max_value, 0.)
        self.assertEqual(micro_annot, 0)

    def peak_inside_test(self):
        """ peak_inside_test2: peak is inside the active window """

        source_path = os.path.join(source_dir, 'pre_impact_test/one_peak_source.csv')
        target_path = os.path.join(source_dir, 'pre_impact_test/one_peak_target.csv')

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
        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertTrue(impact_flag)
        self.assertEqual(max_value,3)
        self.assertEqual(micro_annot,2)

    def peak_inside_test2(self):
        """ peak_inside_test2: peak is inside the active window -- using artificial data """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[185] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(400, len(result_list))
        self.assertTrue(impact_flag)
        self.assertEqual(max_value,3.0)
        self.assertEqual(micro_annot,2.0)

    def peak_in_buffer_test(self):
        """ peak_in_buffer_test2: peak is before active window """

        source_path = os.path.join(source_dir, 'pre_impact_test/peak_in_buffer_source.csv')
        target_path = os.path.join(source_dir, 'pre_impact_test/zero_peak_target.csv')

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
        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,1.0438264405)
        self.assertEqual(micro_annot,0)

    def peak_in_buffer_test2(self):
        """ peak_in_buffer_test2: peak is before active window -- using artificial data"""

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[30] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(200, len(result_list))

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,0)
        self.assertEqual(micro_annot,0)

    def peak_after_window_test(self):
        """ peak_in_buffer_test2: peak is before active window """
        source_path = os.path.join(source_dir, 'pre_impact_test/peak_after_window_source.csv')
        target_path = os.path.join(source_dir, 'pre_impact_test/zero_peak_target.csv')

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
        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        for i in range(len(target_list)):
            target_element_len = len(target_list[0])
            for j in range(target_element_len):
                self.assertEqual(target_list[i][j],result_list[i][j])

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,1.0438264405)
        self.assertEqual(micro_annot,0)

    def peak_after_window_test2(self):
        """ peak_after_window_test2: peak is after the active window """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[350] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(200, len(result_list))

        self.assertEqual(impact_flag,False)
        self.assertEqual(max_value,0)
        self.assertEqual(micro_annot,0)

    def peak_exact_before_window_test(self):
        """ peak_exact_before_window_test: peak is exactly before the active window """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[99] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(200, len(result_list))

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,0)
        self.assertEqual(micro_annot,0)

    def peak_exact_inside_window_test(self):
        """ peak_exact_inside_window_test: peak is exactly at the beginning of the active window """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[100] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(400, len(result_list))

        self.assertTrue(impact_flag)
        self.assertEqual(max_value,3.)
        self.assertEqual(micro_annot,2)


    def peak_exact_end_window_test(self):
        """ peak_exact_end_window_test: peak is exactly at the end of the active window """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[299] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(400, len(result_list))

        self.assertTrue(impact_flag)
        self.assertEqual(max_value,3.)
        self.assertEqual(micro_annot,2)


    def peak_exact_after_window_test(self):
        """ peak_exact_after_window_test: peak is exactly after the active window """

        zeros = ARRAY_TUPLED(*([0.] * 18))

        general_buffer = [zeros] * 400

        general_buffer[300] = zeros._replace(AVMC=3.,
                                             ANNOTCHEST=2)
        freq_rate = 100 #sampling freq_rate

        result_list,impact_flag,max_value,max_index,micro_annot, run_time = cascade_with_rule.pre_impact_phase(general_buffer, freq_rate, 0, 0, 0)

        self.assertEqual(200, len(result_list))

        self.assertFalse(impact_flag)
        self.assertEqual(max_value,0)
        self.assertEqual(micro_annot,0)

if __name__ == '__main__':
    unittest.main()
