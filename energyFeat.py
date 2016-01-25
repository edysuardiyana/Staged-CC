__author__ = 'ArseneLupin'


import numpy
import integrator

def energyCalc(array1,array2,array3):

  totEnergy = integrator.integrate(numpy.array(array1) ** 2) + integrator.integrate(numpy.array(array2) ** 2) + \
              integrator.integrate(numpy.array(array3) ** 2)

  return totEnergy

