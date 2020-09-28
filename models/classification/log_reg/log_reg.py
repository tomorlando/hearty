

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import sklearn
import matplotlib as plt
import pickle
import joblib


df = pd.read_csv('/Users/Tom Orlando/Monash/FIT3164/data/filtered_features/heart_train.csv')
y_train = df.CAD_Yes.values
x_train = df.drop(['CAD_Yes'], axis=1)

df = pd.read_csv('/Users/Tom Orlando/Monash/FIT3164/data/filtered_features/heart_test.csv')
y_test = df.CAD_Yes.values
x_test = df.drop(['CAD_Yes'], axis=1)

model = LogisticRegression()
scaler = MinMaxScaler(feature_range = (0,1))

scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)
y_pred

confusion_matrix(y_test, y_pred)

param_grid = [
              {'penalty': ['l1', 'l2'],
               'C': np.logspace(-4,4,20),
               'solver': ['liblinear']}
              ]

grid_search = GridSearchCV(model, param_grid, cv = 5, scoring='accuracy', n_jobs=-1)

grid_search.fit(x_train, y_train)

final_model = grid_search.best_estimator_

y_pred = final_model.predict(x_test)

confusion_matrix(y_test, y_pred)

print(classification_report(y_test,y_pred))
print("recall score", recall_score(y_test, y_pred))
print("f1_score", f1_score(y_test, y_pred))
print("precision", precision_score(y_test, y_pred))

sklearn.metrics.plot_roc_curve(final_model, x_test, y_test)
sklearn.metrics.plot_confusion_matrix(final_model, x_test, y_test, cmap='Blues')

joblib.dump(final_model, 'log_reg.pkl')
joblib.dump(scaler, 'scaler.pkl')


user_test = [[ 1, 25,  1,  1,  1, 45, 85,  3,  1,  1, 78, 45, 59,  1,  1]]

