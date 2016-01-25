__author__ = 'ArseneLupin'

import scale_file
import unittest
import math

class general_scaling_test(unittest.TestCase):

    def general_scaling_test(self):

        """general_scaling_test: This is a test to check the scaling process in general"""

        x_chest_val = 2308.000
        y_chest_val = 2078.000
        z_chest_val = 1951.000

        x_chest_g = 1834.000
        y_chest_g = 1833.000
        z_chest_g = 1861.000

        x_waist_val = 2321.000
        y_waist_val = 2039.000
        z_waist_val = 1988.000

        x_waist_g = 1865.000
        y_waist_g = 1883.000
        z_waist_g = 1808.000

        x_thigh_val = 2326.000
        y_thigh_val = 1996.000
        z_thigh_val = 2130.000

        x_thigh_g = 1825.000
        y_thigh_g = 1826.000
        z_thigh_g = 1858.000

        input_list = [0, x_chest_val, y_chest_val, z_chest_val, x_chest_g, y_chest_g, z_chest_g,0,0, x_waist_val, y_waist_val, z_waist_val,
                     x_waist_g, y_waist_g, z_waist_g, 0, 0, x_thigh_val, y_thigh_val, z_thigh_val, x_thigh_g, y_thigh_g, z_thigh_g, 0, 0,
                     0, 0, 0, 0, 0, 0]
        output_list = scale_file.scale_row(input_list)

        output_target = [0.939823387096774, 0.154050268817204, -0.171498655913979, 2.56316367630904, 1.46466495789088,
                         -1.46466495789088, 0.9676834571475359, 3.29549615525448, 0.947475403225806, 0.0440576612903226, 0.268543010752688,
                         0.732332478945441, -1.8308311973636, 0.366166239472721, 0.9857819565504304, 2.0055750915604738,0]


        for i in range(len(output_list)):
             self.assertAlmostEqual(output_list[i],output_target[i])

if __name__ == '__main__':
    unittest.main()
