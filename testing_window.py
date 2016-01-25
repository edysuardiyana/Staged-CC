""" test out idea about windowing """

import numpy as np


def main():
    w = [1.0] * 700
    #w[0] = 1.7
    #w[100] = 1.8
    #w[200] = 1.9
    #w[400] = 1.9
    #w[250] = 1.9
    #w[600] = 1.9
    #w[395] = 4
    #w[302] = 1.65
    #w[100] = 1.64
    #w[300] = 1.8

    vm = np.array(w)
    peaks = np.argwhere(vm > 1.6)

    active_peak = None
    temp = None
    for i in range(len(peaks)):
        #not in buffer
        if peaks[i][0]>=100:
            #not in edge
            if peaks[i] < 300:
                #inside 2 secs window
                if temp is None:
                    temp = peaks[i][0]
                if i > 0:
                    if peaks[i]-200 < peaks[i-1]:
                        if vm[peaks[i-1]] >= vm[peaks[i]]:
                            temp = peaks[i-1][0]
                        else:
                            temp = peaks[i][0]
                    else:
                        active_peak = temp
                        temp = None

    if temp is not None:
        active_peak = temp

    print active_peak

if __name__ == "__main__":
    main()
