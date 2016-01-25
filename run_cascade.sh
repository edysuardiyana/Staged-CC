nosetests testcase/ --exe

python main.py

export CLASSPATH=/Applications/weka-3-6-10/weka.jar:/Applications/weka-3-6-10/libsvm.jar

FOLDER_PATH="/Users/ArseneLupin/Documents/edy/experiment_new_cascade/"

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $VARIABLE
java weka.classifiers.lazy.IBk -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/knn/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $VARIABLE
java weka.classifiers.trees.J48 -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/J48/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29",,"subject_31","tyo","victor"}

do
echo $VARIABLE
java weka.classifiers.functions.Logistic -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/Logistic/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}

do
echo $VARIABLE
java weka.classifiers.functions.MultilayerPerceptron -L 0.3 -M 0.2 -E 20 -H "5,4,3" -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/multi/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $VARIABLE
java weka.classifiers.functions.LibSVM -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/svm/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $VARIABLE
java weka.classifiers.functions.LibSVM -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/svm/"$VARIABLE".txt
done

for VARIABLE in {"bimo","daniella","dawan","dimitrios","gabriella","herdi","jessica","kao","lawal","lukas","madeline","muhammad_bag","musaab","naufal","raedi","rines","salieu","subject_1","subject_2","subject_3","subject_4","subject_5","subject_6","subject_7","subject_8","subject_9","subject_10","subject_11","subject_12","subject_13","subject_14","subject_15","subject_16","subject_17","subject_19","subject_20","subject_21","subject_22","subject_24","subject_25","subject_26","subject_28","subject_29","subject_31","tyo","victor"}
do
echo $VARIABLE
java weka.classifiers.functions.LibSVM -t "$FOLDER_PATH"/trainingweka/"$VARIABLE"-training.arff -T "$FOLDER_PATH"/weka/"$VARIABLE".arff -i > "$FOLDER_PATH"/result/svm/"$VARIABLE".txt
done
