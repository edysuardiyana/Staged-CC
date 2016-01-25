__author__ = 'ArseneLupin'



def writeWeka(source,dest):
    #dest= '/home/edy/S3/weka/bimo.arff'
    #source = "/home/edy/S3/featuresnew/bimo_feat.csv"
    objectwrite = open(source)
    data=[]
    stringtemp=''
    comment = '%'+source
    relation= '@relation falls'
    attribute1 = '@attribute MinimumValuePre real'
    attribute2 = '@attribute MinimumValueImp real'
    attribute3 = '@attribute MinimumValuePost real'
    attribute4 = '@attribute MaximumValuePre real'
    attribute5 = '@attribute MaximumValueImp real'
    attribute6 = '@attribute MaximumValuePost real'
    attribute7 = '@attribute MeanPreImpact real'
    attribute8 = '@attribute MeanImpact real'
    attribute9 = '@attribute MeanPostImpact real'
    attribute10 = '@attribute RootMeanSquarePreImpact real'
    attribute11 = '@attribute RootMeanSquareImpact real'
    attribute12 = '@attribute RootMeanSquarePostImpact real'
    attribute13= '@attribute VariancePreImpact real'
    attribute14= '@attribute VarianceImpact real'
    attribute15= '@attribute VariancePostImpact real'
    attribute16= '@attribute VelocityPreImpact real'
    attribute17= '@attribute VelocityImpact real'
    attribute18= '@attribute VelocityPostImpact real'
    attribute19= '@attribute EnergyPreImpact real'
    attribute20= '@attribute EnergyImpact real'
    attribute21= '@attribute EnergyPostImpact real'
    attribute22= '@attribute SignalMagnitudeAreaPreImpact real'
    attribute23= '@attribute SignalMagnitudeAreaImpact real'
    attribute24= '@attribute SignalMagnitudeAreaPostImpact real'
    attribute25= '@attribute ExponentialMovingAveragePreImpact real'
    attribute26= '@attribute ExponentialMovingAverageImpact real'
    attribute27= '@attribute ExponentialMovingAveragePostImpact real'
    #attribute24= '@attribute VectorMagnitude real'
    attribute28= '@attribute annotation {0.0,2.0}'


    for line in objectwrite:
        datatemp = line.split()
        stringdata = ",".join(datatemp)
        data.append(stringdata)

    #listWrite = [relation,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7,attribute8,attribute9,
    #             attribute10,attribute11,attribute12,attribute13,attribute14,attribute15,attribute16,attribute17,attribute18,
    #             attribute19,attribute20,attribute21,attribute22,attribute23,attribute24,attribute30]

    listWrite = [relation,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7,attribute8,attribute9,
                 attribute10,attribute11,attribute12,attribute13,attribute14,attribute15,attribute16,attribute17,attribute18,
                 attribute19,attribute20,attribute21,attribute22,attribute23,attribute24,attribute25,
                 attribute26,attribute27,attribute28]

    fileopen = open(dest,'w')

    print 'Writing the features into arff file'
    for i in range(len(listWrite)):
        fileopen.write(listWrite[i]+'\n')

    fileopen.write('\n')
    fileopen.write('@data\n')
    fileopen.write('\n')

    for j in range(len(data)):
        fileopen.write(data[j]+'\n')

    fileopen.close()

    print 'Finish writing'
