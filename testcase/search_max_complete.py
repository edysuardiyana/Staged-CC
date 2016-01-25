import unittest
import searchmax
import numpy as np
from collections import namedtuple

class searchMaximum(unittest.TestCase):

    #this is a test case for the sequence that has only one peak
    def base_case_test(self):

        """base_case_test: this test is used to check the function for searching the maximum value -- using artificial data"""


        
        ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
        ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')
        target_list_base = [[[1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,0]],
        [[2,2,2,2,2,2,2,2,0],[2,2,2,2,2,2,2,2,2,0]],
        [[3,3,3,3,3,3,3,3,2],[3,3,3,3,3,3,3,3,0]]]

        source_list= [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2]]

        data_pool_base=[]

        for temp_data in source_list:
            source_line = ARRAY_TUPLED(*temp_data)
            data_pool_base.append(source_line)

        result_list = searchmax.micAn(data_pool_base)

        for i in range(len(target_list_base)):
            for j in range(len(target_list_base[0])):
                temp = target_list_base[0]
                for k in range(len(temp)):
                    self.assertAlmostEqual(target_list_base[i][j][k], result_list[i][j][k])
