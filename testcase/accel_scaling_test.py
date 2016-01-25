__author__ = 'ArseneLupin'

import ascale
import unittest

class accelScalingTest(unittest.TestCase):

    def accel_sens_1_test(self):

        """accel_sens_1_test: this function tests the scaling function for gyro that was strapped on chest"""

        x_val = 2308.000
        y_val = 2078.000
        z_val = 1951.000

        #chest sensor
        scaled_x = ascale.ascale(x_val,1,1)
        scaled_y = ascale.ascale(y_val,1,2)
        scaled_z = ascale.ascale(z_val,1,3)

        self.assertAlmostEqual(scaled_x,0.939823387096774)
        self.assertAlmostEqual(scaled_y,0.154050268817204)
        self.assertAlmostEqual(scaled_z,-0.171498655913979)


    def accel_sens_2_test(self):

        """accel_sens_2_test: this function tests the scaling function for gyro that was strapped on waist"""

        x_val = 2326.000
        y_val = 1996.000
        z_val = 2130.000

        #thigh sensor
        scaled_x = ascale.ascale(x_val,3,1)
        scaled_y = ascale.ascale(y_val,3,2)
        scaled_z = ascale.ascale(z_val,3,3)

        self.assertAlmostEqual(scaled_x,0.947475403225806)
        self.assertAlmostEqual(scaled_y,0.0440576612903226)
        self.assertAlmostEqual(scaled_z,0.268543010752688)

    def accel_sens_3_test(self):

        """accel_sens_1_test: this function tests the scaling function for gyro that was strapped on thigh"""


        x_val = 2321.000
        y_val = 2039.000
        z_val = 1988.000

        #waist sensor
        scaled_x = ascale.ascale(x_val,2,1)
        scaled_y = ascale.ascale(y_val,2,2)
        scaled_z = ascale.ascale(z_val,2,3)

        self.assertAlmostEqual(scaled_x,0.999040994623656)
        self.assertAlmostEqual(scaled_y,-0.0213913978494624)
        self.assertAlmostEqual(scaled_z,-0.115532258064516)

if __name__ == '__main__':
    unittest.main()
