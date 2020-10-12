#install package skelean,pandas first
import sklearn
from sklearn import svm
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score
from sklearn import metrics
import joblib
from sklearn.model_selection import cross_val_score
import pandas as pd

#Read external data
Cad_train = pd.read_csv('/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_train.csv')
#extract Xand Y
Y_train = Cad_train.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
#Read external data
Cad_test = pd.read_csv('/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_train.csv')
#extract Xand Y
Y_test = Cad_test.CAD_Yes.values
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)

from sklearn.svm import SVC
from sklearn import metrics
#The fit method of SVC class is called to train the algorithm on the training data, which is passed as a parameter to the fit method
# fit a SVM model to the data
svcclassifier=SVC(kernel='linear')

svcclassifier.fit(X_train, Y_train)
#To make predictions, the predict method of the SVC class is used.
y_pred = svcclassifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix
#Evaluating the Algorithm
print(confusion_matrix(Y_test,y_pred))
print(classification_report(Y_test,y_pred))
print("recall score",recall_score(Y_test, svcclassifier.predict(X_test)))
print("f1_score",f1_score(Y_test, svcclassifier.predict(X_test)))
print("precision",precision_score(Y_test, svcclassifier.predict(X_test)))
sklearn.metrics.plot_roc_curve(svcclassifier, X_test, Y_test)
sklearn.metrics.plot_confusion_matrix(svcclassifier, X_test, Y_test, cmap='Blues')
scores = cross_val_score(svcclassifier, X_train, Y_train, cv=10, scoring="accuracy")
print(scores)
meanScore = scores.mean()
print(meanScore * 100)

joblib.dump(svcclassifier, 'svm_model.pkl')
