__author__ = 'ArseneLupin'

import unittest
import searchmax
import numpy as np
from collections import namedtuple

class searchMaxMicrotest(unittest.TestCase):
    def micro_test(self):

    """micro_test: this test is used to check the function for searching the maximum value"""

        ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                                 ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')

        data_pool =[]

        targetList = [[[0.9398233871,0.1540502688,-0.1714986559,2.5631636763,1.4646649579,-1.4646649579,0.9676834571,
                              3.2954961553,2],[0.9474754032,0.0440576613,0.2685430108,0.7323324789,-1.8308311974,0.3661662395,
                              0.9857819566,2.0055750916,0]],
                      [[0.9261432796,0.1331620968,-0.1741370968,2.9293299158,
                              2.9293299158,-1.8308311974,0.9517338109,4.5292262456,0],[0.9685012097,0.0307068548,0.2496505376,0.3661662395,
                              -0.7323324789,0.7323324789,1.0006312483,1.0984987184,2]],
                      [[0.9179352151,0.1305510753,-0.1926061828,1.0984987184,
                              5.1263273526,-1.0984987184,0.9469666224,5.3565502887,2],[0.9553600806,0.0146858871,0.2577473118,-0.7323324789,
                              -1.4646649579,0.7323324789,0.9896273216,1.7938408955,0]]]

        rawsourceList = [[0.9398233871,0.1540502688,-0.1714986559,2.5631636763,1.4646649579,-1.4646649579,0.9676834571,3.2954961553,
                       0.9474754032,0.0440576613,0.2685430108,0.7323324789,-1.8308311974,0.3661662395,0.9857819566,2.0055750916,2],
                      [0.9261432796,0.1331620968,-0.1741370968,2.9293299158,2.9293299158,-1.8308311974,0.9517338109,4.5292262456,
                       0.9685012097,0.0307068548,0.2496505376,0.3661662395,-0.7323324789,0.7323324789,1.0006312483,1.0984987184,2],
                      [0.9179352151,0.1305510753,-0.1926061828,1.0984987184,5.1263273526,-1.0984987184,0.9469666224,5.3565502887,
                       0.9553600806,0.0146858871,0.2577473118,-0.7323324789,-1.4646649579,0.7323324789,0.9896273216,1.7938408955,2]]

        for temp_data in rawsourceList:
            sourceList = ARRAY_TUPLED(*temp_data)
            data_pool.append(sourceList)

        resultList = searchmax.micAn(data_pool)
        #self.assertAlmostEqual(targetListnonFalls,sourceListnonFalls)


        for i in range(len(targetList)):
            for j in range(len(targetList[0])):
                temp = targetList[0]
                for k in range(len(temp)):
                    self.assertAlmostEqual(targetList[i][j][k],resultList[i][j][k])

    #def empty_test(self):
        #x = searchmax.micAn([])
        #self.assertEquals(len(x), 0)

    #def one_element_test(self):
        #x = searchmax.micAn([[1.0] * 16])
        #self.assertEquals(x[0][16] = 2)

    #def changes_size_correctly_test(self):
        #x = searchmax.micAn([[1.0] * 16] * 4)
        #for i in x:
            #self.assertEquals(len(i), 17)

if __name__ == '__main__':
    unittest.main()
