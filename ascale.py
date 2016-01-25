__author__ = 'ArseneLupin'

#this program is used to convert raw data value from accelerometer and gyroscope

CONSTANT_VAL = 372
CHEST_SENS = [(1964.5, 1.0178),(2019, 0.9713),(2016, 0.9815)]
WAIST_SENS = [(1948.5, 0.9977),(2047, 0.9947),(2031.5, 0.9880)]
THIGH_SENS = [(1965.5, 0.9777),(1979.5, 0.9933),(2030.5, 1.0040)]

def ascale(rawval, sensor, axis):

    if sensor == 1:  #sensor node 1 (Chest E131)
        if axis == 1:
            midval = CHEST_SENS[0][0]
            sencor = CHEST_SENS[0][1]
        elif axis == 2:
            midval = CHEST_SENS[1][0]
            sencor = CHEST_SENS[1][1]
        else:
            midval = CHEST_SENS[2][0]
            sencor = CHEST_SENS[2][1]

    elif sensor == 2:  #sensor node 2 (Waist E021)
        if axis == 1:
            midval = WAIST_SENS[0][0]
            sencor = WAIST_SENS[0][1]
        elif axis == 2:
            midval = WAIST_SENS[1][0]
            sencor = WAIST_SENS[1][1]
        else:
            midval = WAIST_SENS[2][0]
            sencor = WAIST_SENS[2][1]
    else:
        if axis == 1:  #sensor node 3 (Thigh DED2)
            midval = THIGH_SENS[0][0]
            sencor = THIGH_SENS[0][1]
        elif axis == 2:
            midval = THIGH_SENS[1][0]
            sencor = THIGH_SENS[1][1]
        else:
            midval = THIGH_SENS[2][0]
            sencor = THIGH_SENS[2][1]

    val = ((rawval - midval) * sencor) / float(CONSTANT_VAL)

    return val