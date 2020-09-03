#install package skelean,pandas first
from sklearn import svm
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score
from sklearn import metrics

import pandas as pd

#Read external data
Cad_train = pd.read_csv(r'C:\Users\tanji\FIT3164\data\filtered_features\heart_train.csv')
#extract Xand Y
Y_train = Cad_train.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
#Read external data
Cad_test = pd.read_csv(r'C:\Users\tanji\FIT3164\data\filtered_features\heart_test.csv')
#extract Xand Y
Y_test = Cad_test.CAD_Yes.values
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)

from sklearn.svm import SVC
from sklearn import metrics

# fit a SVM model to the data

model_train = SVC()
print(model_train)
model_train.fit(X_train, Y_train)

# make predictions
expected_train =Y_train
predicted_train = model_train.predict(X_train)
# summarize the fit of the model
print(metrics.classification_report(expected_train, predicted_train))
print(metrics.confusion_matrix(expected_train, predicted_train))




# fit a SVM model to the data

model_test = svm.SVC()
print(model_test)
model_test.fit(X_test, Y_test)

# make predictions
expected_test =Y_test
predicted_test = model_test.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected_test, predicted_test))
print(metrics.confusion_matrix(expected_test, predicted_test))

