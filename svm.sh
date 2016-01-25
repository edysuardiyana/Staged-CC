export CLASSPATH=/Applications/weka-3-6-10/weka.jar:/Applications/weka-3-6-10/libsvm.jar

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_18","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do 
echo $VARIABLE
java weka.classifiers.functions.LibSVM -t trainingweka/"$VARIABLE"-training.arff -T weka/"$VARIABLE".arff -i > result/svm/"$VARIABLE".txt
done
