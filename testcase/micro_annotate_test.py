__author__ = 'ArseneLupin'

import unittest
import microannotate_right
import os

class searchMaxMicrotest(unittest.TestCase):
    def micro_test(self):

        """micro_test: this function checks the micro-annotation function"""
        source_dir = os.path.dirname(os.path.realpath(__file__))
        source_path = os.path.join(source_dir, 'micro_annotate_test')
        targetList = [[[0.7975502688, 0.005222043, -0.5171344086, 4.3939948737, 5.1263273526, 1.8308311974, 0.9505481038,
                      6.9955961825, 0],[0.9106802419, 0.1321729839, 0.3711021505, 2.1969974368, -1.4646649579, -3.6616623947,
                      0.9922323351,4.514400588,0]],
                      [[0.8194384409, -0.010444086, -0.5303266129, 3.6616623947, 5.4924935921, 2.5631636763, 0.9761325492,
                       7.0813180541, 0],[0.8896544355, 0.1375133065, 0.3818978495, 2.9293299158, -2.1969974368, -3.2954961553,
                       0.9778757035, 4.9262629246, 0]],
                      [[0.8167024194, -0.005222043, -0.5303266129, 2.5631636763, 4.7601611131, 2.1969974368, 0.9737948592,
                       5.8357295681, 2],[0.9185649194, 0.1348431452, 0.3684032258, 2.9293299158, -1.4646649579, -3.2954961553, 0.9988318786,
                       4.6461287222, 2]],
                      [[0.8194384409, 0, -0.5039422043, 2.5631636763, 5.1263273526, 2.5631636763, 0.9619964156, 6.2784431342,0],
                       [0.8949108871, 0.142853629, 0.3738010753, 2.5631636763, -2.1969974368, -3.2954961553, 0.9803060232,
                        4.7177219798, 0]],
                      [[0.8221744624, -0.005222043, -0.5171344086, 3.2954961553, 4.7601611131, 2.5631636763,
                        0.9713012472 , 6.3316061757, 0],[ 0.8975391129,0.1375133065, 0.3711021505, 2.1969974368, -2.5631636763,
                        -3.6616623947, 0.9809195557, 4.9803993075, 0]],
                      [[0.8030223118, 0.015666129, -0.5118575269, 4.3939948737, 4.7601611131, 2.1969974368, 0.9524118798,
                       6.840549869, 0], [0.9106802419, 0.1268326613, 0.3872956989, 2.1969974368, -1.8308311974, -3.6616623947,
                       0.9977088681, 4.6461287222, 0]]]


        resultList = microannotate_right.micro_annotate_search(source_path)
        #self.assertAlmostEqual(targetListnonFalls,sourceListnonFalls)


        for i in range(len(targetList)):
            for j in range(len(targetList[0])):
                temp = targetList[0]
                for k in range(len(temp)):
                    self.assertAlmostEqual(targetList[i][j][k],resultList[i][j][k])

if __name__ == '__main__':
    unittest.main()
