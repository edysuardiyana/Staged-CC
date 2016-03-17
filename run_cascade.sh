#nosetests testcase/ --exe

#python main.py

export CLASSPATH=/home/edysuardiyana/edy/weka-3-6-13/weka.jar:/home/edysuardiyana/edy/weka-3-6-13/libsvm.jar

java -Xmx1024m -jar /home/edysuardiyana/edy/weka-3-6-13/weka.jar
FOLDER_PATH="/home/edysuardiyana/edy/experiment_new_cascade"
TRAINING_PATH="/media/edysuardiyana/4A38F6CC38F6B653/Users/43770673"

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $TRAINING_PATH/training_weka/$VARIABLE-training.arff
java weka.classifiers.trees.J48 -t $TRAINING_PATH/training_weka/$VARIABLE-training.arff -T $FOLDER_PATH/weka/$VARIABLE.arff -i > $FOLDER_PATH/result/J48/$VARIABLE.txt
done

#for VARIABLE in "bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29",,"subject_31","tyo","victor"
#do
#echo $VARIABLE
#java weka.classifiers.functions.Logistic -t $TRAINING_PATH/training_weka/$VARIABLE-training.arff -T $FOLDER_PATH/weka/$VARIABLE.arff -i > $FOLDER_PATH/result/Logistic/$VARIABLE.txt
#done

#for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
#do
#echo $VARIABLE
#java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -E 20 -H "5,4,3" -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/multi/"$VARIABLE".txt
#done

#for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
#do
#echo $VARIABLE
#java weka.classifiers.functions.LibSVM -t "$TRAINING_PATH"/training_weka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/svm/"$VARIABLE".txt
#done
