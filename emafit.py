__author__ = 'ArseneLupin'

#this code is calculating EMA value

CONST_ALPHA =  0.01 #float(2)/(len(arrdat)+1) # this is calculated by : 2/N+1 where N is total number of the data

def ema(arrdat):

    sem=[]

    for i in range(0,len(arrdat)):

        if i == 0:
            sval = 0

        else:
            sval = (CONST_ALPHA * arrdat[i]) + (1-CONST_ALPHA) * sem[i-1]

        sem.append(sval)


    emval = sem[len(sem)-1]

    return emval
