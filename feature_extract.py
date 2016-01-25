__author__ = 'ArseneLupin'

#this code is for calculating and combining the features
from numpy import sqrt, mean
import numpy
import integrator
import emafit
import csv
import energyFeat
import smaFeat


def calc_features(fullarray,micannot,samp_rate):

    #vect_c not used

    pre_win = [0,samp_rate] #pre-window
    imp_win = [samp_rate,samp_rate*2] # impact window
    post_win = [samp_rate*2, samp_rate*5] #post impact window

    datAr = [] #for vector magnitude
    datXa= [] #for X values
    datYa= [] #for Y values
    datZa= [] #for Z values

    datXg=[]
    datYg=[]
    datZg=[]

    for tempdata in fullarray:
        datAr.append(float(tempdata[6]))
        datXa.append(float(tempdata[0]))
        datYa.append(float(tempdata[1]))
        datZa.append(float(tempdata[2]))

        datXg.append(float(tempdata[3]))
        datYg.append(float(tempdata[4]))
        datZg.append(float(tempdata[5]))

    #******************************************************************************************************************************
    #minimum pre impact
    min_pre = min(datAr[pre_win[0]:pre_win[1]])

    #minimum value impact
    min_imp = min(datAr[imp_win[0]:imp_win[1]])

    #minimum post imp
    min_post = min(datAr[post_win[0]:post_win[1]])

    #******************************************************************************************************************************
    #maximum value pre-impact
    max_pre = max(datAr[pre_win[0]:pre_win[1]])

    #maximum value impact
    max_imp = max(datAr[imp_win[0]:imp_win[1]])

    #maximum value post
    max_post = max(datAr[post_win[0]:post_win[1]])
    #******************************************************************************************************************************
    #mean for pre-impact event
    meanList1 = datAr[pre_win[0]:pre_win[1]]
    meanVal1 = numpy.mean(meanList1)

    #******************************************************************************************************************************
    #mean for impact
    meanList2 = datAr[imp_win[0]:imp_win[1]]
    meanVal2 = numpy.mean(meanList2)

    #******************************************************************************************************************************
    #mean for post-impact
    meanList3 = datAr[post_win[0]:post_win[1]]
    meanVal3 = numpy.mean(meanList3)

    #******************************************************************************************************************************
    #Root mean square for pre-impact
    rmsList1 = datAr[pre_win[0]:pre_win[1]]
    rms1 = sqrt(mean(numpy.array(rmsList1)**2))

    #Root mean square for impact
    rmsList2 = datAr[imp_win[0]:imp_win[1]]
    rms2 = sqrt(mean(numpy.array(rmsList2)**2))

    #Root mean square for post-impact
    rmsList3 = datAr[post_win[0]:post_win[1]]
    rms3 = sqrt(mean(numpy.array(rmsList3)**2))

    #******************************************************************************************************************************
    #variance for pre-impact
    variance1 = numpy.var(datAr[pre_win[0]:pre_win[1]],ddof=1)

    #variance for impact
    variance2 = numpy.var(datAr[imp_win[0]:imp_win[1]],ddof=1)

    #variance for post-impact
    variance3 = numpy.var(datAr[post_win[0]:post_win[1]],ddof=1)

    #******************************************************************************************************************************
    #velocity in pre-impact
    velo1 = integrator.integrate(datAr[pre_win[0]:pre_win[1]])

    #velocity in impact
    velo2 = integrator.integrate(datAr[imp_win[0]:imp_win[1]])

    #velocity in post-impact
    velo3 = integrator.integrate(datAr[post_win[0]:post_win[1]])

    #******************************************************************************************************************************
    #energy in pre-impact
    win1x = datXa[pre_win[0]:pre_win[1]]
    win1y = datYa[pre_win[0]:pre_win[1]]
    win1z = datZa[pre_win[0]:pre_win[1]]
    energy1 = energyFeat.energyCalc(win1x,win1y,win1z)

    #energy in impact
    win2x = datXa[imp_win[0]:imp_win[1]]
    win2y = datYa[imp_win[0]:imp_win[1]]
    win2z = datZa[imp_win[0]:imp_win[1]]
    energy2 = energyFeat.energyCalc(win2x,win2y,win2z)

     #energy in post-impact
    win3x = datXa[post_win[0]:post_win[1]]
    win3y = datYa[post_win[0]:post_win[1]]
    win3z = datZa[post_win[0]:post_win[1]]
    energy3 = energyFeat.energyCalc(win3x,win3y,win3z)

    #******************************************************************************************************************************
    #signal magnitude are in pre-impact
    sma1 = smaFeat.smafeat(datXa[pre_win[0]:pre_win[1]],datYa[pre_win[0]:pre_win[1]],datZa[pre_win[0]:pre_win[1]])

    #signal magnitude are in impact
    sma2 = smaFeat.smafeat(datXa[imp_win[0]:imp_win[1]],datYa[imp_win[0]:imp_win[1]],datZa[imp_win[0]:imp_win[1]])

    #signal magnitude are in pre-impact
    sma3 = smaFeat.smafeat(datXa[post_win[0]:post_win[1]],datYa[post_win[0]:post_win[1]],datZa[post_win[0]:post_win[1]])
    #******************************************************************************************************************************
    #exponential moving average in pre-impact
    ewma1 = emafit.ema(datAr[pre_win[0]:pre_win[1]])

    #exponential moving average in impact
    ewma2 = emafit.ema(datAr[imp_win[0]:imp_win[1]])

    #exponential moving average in post-impact
    ewma3 = emafit.ema(datAr[post_win[0]:post_win[1]])

    #******************************************************************************************************************************

    datfeat = [min_pre,min_imp,min_post, max_pre, max_imp, max_post, meanVal1, meanVal2, meanVal3, rms1, rms2, rms3, variance1,
    variance2, variance3, velo1,velo2, velo3, energy1, energy2, energy3, sma1, sma2, sma3, ewma1, ewma2, ewma3, micannot]

    return datfeat


#datfeat = [minVal, maxVal, meanVal1, meanVal2, meanVal3, rms1, rms2, rms3, variance1, variance2, variance3, velo1,
#          velo2, velo3, energy1, energy2, energy3, sma1, sma2, sma3, ewma1, ewma2, ewma3, annot]


#datfeat = [minVal, maxVal, meanVal1, meanVal2, meanVal3, rms1, rms2, rms3, variance1, variance2, variance3, velo1,
#          velo2, velo3, energy1, energy2, energy3, sma1, sma2, sma3, ewma1, ewma2, ewma3, annot]

#datfeat = [minVal, maxVal, meanVal1, meanVal2, meanVal3, rms1, rms2, rms3, variance1, variance2, variance3, velo1,
#           velo2, velo3, energy1, energy2, energy3, sma1, sma2, sma3, ewma1, ewma2, ewma3, angle_y_1, angle_z_1,
#           angle_y_2, angle_z_2,angle_y_3,angle_z_3, annot]
#******************************************************************************************************************************
#Tilt Angle in pre-impact
#all_angle_1 = mytilt.mytilt(datXa[pre_win[0]:pre_win[1]],datYa[pre_win[0]:pre_win[1]],datZa[pre_win[0]:pre_win[1]],
#                            datXg[pre_win[0]:pre_win[1]],datYg[pre_win[0]:pre_win[1]],datZg[pre_win[0]:pre_win[1]])
#angle_y_1 = numpy.max(numpy.abs(numpy.array(all_angle_1[0])))
#angle_z_1 = numpy.max(numpy.abs(numpy.array(all_angle_1[1])))

#Tilt Angle in impact
#all_angle_2 = mytilt.mytilt(datXa[tilt_sample_impact[0]:tilt_sample_impact[1]],datYa[tilt_sample_impact[0]:tilt_sample_impact[1]],
#                           datZa[tilt_sample_impact[0]:tilt_sample_impact[1]],datXg[tilt_sample_impact[0]:tilt_sample_impact[1]],
#                          datYg[tilt_sample_impact[0]:tilt_sample_impact[1]],datZg[tilt_sample_impact[0]:tilt_sample_impact[1]])
#angle_y_2 = numpy.max(numpy.abs(numpy.array(all_angle_2[0])))
#angle_z_2 = numpy.max(numpy.abs(numpy.array(all_angle_2[1])))

#Tilt Angle in post-impact
#all_angle_3 = mytilt.mytilt(datXa[tilt_sample_post[0]:tilt_sample_post[1]],datYa[tilt_sample_post[0]:tilt_sample_post[1]],
#                          datZa[tilt_sample_post[0]:tilt_sample_post[1]],datXg[tilt_sample_post[0]:tilt_sample_post[1]],
#                          datYg[tilt_sample_post[0]:tilt_sample_post[1]],datZg[tilt_sample_post[0]:tilt_sample_post[1]])
#angle_y_3 = numpy.max(numpy.abs(numpy.array(all_angle_3[0])))
#angle_z_3 = numpy.max(numpy.abs(numpy.array(all_angle_3[1])))
