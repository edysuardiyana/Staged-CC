__author__ = 'ArseneLupin'


from collections import namedtuple


ARRAY_TUPLED = namedtuple('ARRAY_TUPLED', 'AXC AYC AZC GXC GYC GZC AVMC GVMC'
                                 ' AXT AYT AZT GXT GYT GZT AVMT GVMT ANNOT')
def reanotright(raw_data):

    arrdata=[]
    chestData=[]
    #waistData=[]
    thighData=[]

    arr_tupled = ARRAY_TUPLED(*raw_data)

    chestData = [arr_tupled.AXC,arr_tupled.AYC,arr_tupled.AZC,arr_tupled.GXC,arr_tupled.GYC,arr_tupled.GZC,arr_tupled.AVMC,arr_tupled.GVMC, 0]
    thighData = [arr_tupled.AXT, arr_tupled.AYT, arr_tupled.AZT, arr_tupled.GXT, arr_tupled.GYT, arr_tupled.GZT, arr_tupled.AVMT, arr_tupled.GVMT, 0]
    #waistData = [arr[16],arr[17],arr[18],arr[19],arr[20],arr[21],arr[22],arr[23],0]


    arrdata = [chestData,thighData]

    return arrdata
