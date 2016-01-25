__author__ = 'ArseneLupin'

import unittest
import reannotright

class reannot(unittest.TestCase):
    def micro_nonfall_test(self):

        """micro_nonfall_test: this test is used to check the micro-annotation fucntion for non-fall activities"""

        targetList = [[0.9398233871,0.1540502688,-0.1714986559,2.5631636763,1.4646649579,-1.4646649579,0.9676834571,
                              3.2954961553,0],[0.9474754032,0.0440576613,0.2685430108,0.7323324789,-1.8308311974,0.3661662395,
                              0.9857819566,2.0055750916,0]]

        sourceList = [0.9398233871,0.1540502688,-0.1714986559,2.5631636763,1.4646649579,-1.4646649579,0.9676834571,
                              3.2954961553,0.9474754032,0.0440576613,0.2685430108,0.7323324789,-1.8308311974,0.3661662395,
                              0.9857819566,2.0055750916,0]

        resultList = reannotright.reanotright(sourceList)

        for i in range(len(targetList)):
            for j in range(len(targetList[0])):
                self.assertAlmostEqual(targetList[i][j],resultList[i][j])

if __name__ == '__main__':
    unittest.main()
