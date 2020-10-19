"""
author: jiantan
version:4
19/10/2020
This model use decision tree mechine learning algorithm to train dataset, and then evaluate the decision treemodel
"""
#install package skelean,pandas joblibfirst
import joblib
import sklearn
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn.tree import tree
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score

#Read external data
Cad_train = pd.read_csv('/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_train_std.csv')
#extract Xand Y
Y_train = Cad_train.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
#Read external data
Cad_test = pd.read_csv('/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_test_std.csv')
#extract Xand Y
Y_test = Cad_test.CAD_Yes.values
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)


#The fit method of DC class is called to train the algorithm on the training data, which is passed as a parameter to the fit method
# fit a DCmodel to the data

dcclassifier=tree.DecisionTreeClassifier()
dcclassifier.fit(X_train, Y_train)
#To make predictions, the predict method of the DC class is used.
y_pred = dcclassifier.predict(X_test)

#Evaluating the Algorithm
print(confusion_matrix(Y_test,y_pred))
print(classification_report(Y_test,y_pred))
print("recall score",recall_score(Y_test, dcclassifier.predict(X_test)))
print("f1_score",f1_score(Y_test, dcclassifier.predict(X_test)))
print("precision",precision_score(Y_test, dcclassifier.predict(X_test)))
sklearn.metrics.plot_roc_curve(dcclassifier, X_test, Y_test)
sklearn.metrics.plot_confusion_matrix(dcclassifier, X_test, Y_test, cmap='Blues')
scores = cross_val_score(dcclassifier, X_train, Y_train, cv=10, scoring="accuracy")

meanScore = scores.mean()
print("mean score of decision tree is ",meanScore * 100)
#make pkl for decision tree model
joblib.dump(dcclassifier, 'dc_model.pkl')