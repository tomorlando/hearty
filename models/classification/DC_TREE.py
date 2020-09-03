import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.svm import SVC
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
from sklearn.tree import tree
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, Y_train)
y_pred = clf.predict(X_test)
accuracy=accuracy_score(Y_test, y_pred)

print(confusion_matrix(Y_test, y_pred))
print(classification_report(Y_test, y_pred))
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.metrics import log_loss
fpr, tpr, thresholds = roc_curve(Y_test, y_pred)
print(auc(fpr, tpr))
print(log_loss(Y_test, y_pred))