__author__ = 'ArseneLupin'

#this program is for integrating the acceleration value

FREQUENCY = 100

def integrate(arrdat):

    Tperiod = 1/float(FREQUENCY) #calculate period

    velocity = 0; #initial value of velocity

    for n in range(0,len(arrdat)):

        velocity = velocity + arrdat[n] * Tperiod

    return velocity

