#nosetests testcase/ --exe

#python main.py

export CLASSPATH=/home/edysuardiyana/edy/weka-3-6-13/weka.jar:/home/edysuardiyana/edy/weka-3-6-13/libsvm.jar

FOLDER_PATH="/home/edysuardiyana/edy/experiment_new_cascade"

#for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","muhammad_bag","musaab","naufal","raedi","rines","salieu","tyo","victor"}
#do
#echo $TRAINING_PATH/training_weka/$VARIABLE-training.arff
#java weka.classifiers.trees.J48 -t $FOLDER_PATH/training_weka/$VARIABLE-training.arff -T $FOLDER_PATH/weka/$VARIABLE.arff -i > $FOLDER_PATH/result/J48/$VARIABLE.txt
#done

#for VARIABLE in  {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","muhammad_bag","musaab","naufal","raedi","rines","salieu","tyo","victor"}
#do
#echo $VARIABLE
#java weka.classifiers.functions.Logistic -t $FOLDER_PATH/training_weka/$VARIABLE-training.arff -T $FOLDER_PATH/weka/$VARIABLE.arff -i > $FOLDER_PATH/result/Logistic/$VARIABLE.txt
#done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","muhammad_bag","musaab","naufal","raedi","rines","salieu","tyo","victor"}
do
echo $FOLDER_PATH/trainingweka/$VARIABLE-training.arff
java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -E 20 -H "5,4,3" -t $FOLDER_PATH/training_weka/$VARIABLE-training.arff -T $FOLDER_PATH/weka/$VARIABLE.arff -i > $FOLDER_PATH/result/Multi/$VARIABLE.txt
done

#for VARIABLE in  {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","muhammad_bag","musaab","naufal","raedi","rines","salieu","tyo","victor"}
#do
#echo $VARIABLE
#java weka.classifiers.functions.LibSVM -t "$FOLDER_PATH"/training_weka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/svm/"$VARIABLE".txt
#done
