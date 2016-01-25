__author__ = 'ArseneLupin'

import numpy
from numpy import sqrt, mean
import integrator

def smafeat(datXa,datYa,datZa):

    dataXsq1 = sqrt(numpy.array(datXa) ** 2)
    dataYsq1 = sqrt(numpy.array(datYa) ** 2)
    dataZsq1 = sqrt(numpy.array(datZa) ** 2)


    dataXc1 = integrator.integrate(dataXsq1)
    dataYc1 = integrator.integrate(dataYsq1)
    dataZc1 = integrator.integrate(dataZsq1)
    sma = (dataXc1 + dataYc1 + dataZc1) / float(len(dataXsq1))

    return sma



