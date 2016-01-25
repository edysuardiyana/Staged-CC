__author__ = 'ArseneLupin'

import unittest
import gscale

class gyroScalingTest(unittest.TestCase):

    def gyro_Chest_Test(self):
        """gyro_Chest_Test: this function tests the scaling function for gyro that was strapped on chest"""

        x_val = 1834.000
        y_val = 1833.000
        z_val = 1861.000

        x_ref = 1827
        y_ref = 1829
        z_ref = 1865

        #chest gyro
        scaled_x = gscale.gscale(x_val,x_ref)
        scaled_y = gscale.gscale(y_val,y_ref)
        scaled_z = gscale.gscale(z_val,z_ref)

        self.assertAlmostEqual(scaled_x,2.56316367630904)
        self.assertAlmostEqual(scaled_y,1.46466495789088)
        self.assertAlmostEqual(scaled_z,-1.46466495789088)


    def gyro_waist_Test(self):
        """gyro_waist_Test: this function tests the scaling function for gyro that was strapped on waist"""

        x_val = 1865.000
        y_val = 1883.000
        z_val = 1808.000

        x_ref = 1864
        y_ref = 1880
        z_ref = 1810

        #chest gyro
        scaled_x = gscale.gscale(x_val,x_ref)
        scaled_y = gscale.gscale(y_val,y_ref)
        scaled_z = gscale.gscale(z_val,z_ref)

        self.assertAlmostEqual(scaled_x,0.366166239472721)
        self.assertAlmostEqual(scaled_y,1.09849871841816)
        self.assertAlmostEqual(scaled_z,-0.732332478945441)


    def gyro_thigh_Test(self):

        """gyro_thigh_Test: this function tests the scaling function for gyro that was strapped on thigh"""


        x_val = 1825.000
        y_val = 1826.000
        z_val = 1858.000

        x_ref = 1823
        y_ref = 1831
        z_ref = 1857

        #chest gyro
        scaled_x = gscale.gscale(x_val,x_ref)
        scaled_y = gscale.gscale(y_val,y_ref)
        scaled_z = gscale.gscale(z_val,z_ref)

        self.assertAlmostEqual(scaled_x,0.732332478945441)
        self.assertAlmostEqual(scaled_y,-1.8308311973636)
        self.assertAlmostEqual(scaled_z,0.366166239472721)

if __name__ == '__main__':
    unittest.main()
