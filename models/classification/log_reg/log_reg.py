############################################
# File      : log_reg.py
# Project   : FIT3164 project
#
# Date      : 25/10/2020
# Author    : Tom Orlando
# 
# Purpose   : Building out logistic regression
#             model to be used as one of the 
#             classifiers in our project   
############################################

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

# load and intialise training and test set
df = pd.read_csv('./data/filtered_features/heart_train.csv')
y_train = df.CAD_Yes.values
x_train = df.drop(['CAD_Yes'], axis=1)

df = pd.read_csv('./data/filtered_features/heart_test.csv')
y_test = df.CAD_Yes.values
x_test = df.drop(['CAD_Yes'], axis=1)

# initialise logistic regression model and scaler required
model = LogisticRegression()
scaler = MinMaxScaler(feature_range = (0,1))

# fit the scaler on our training data
scaler.fit(x_train)

# transform data in both training and test sets
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# fit the log reg model to training data
model.fit(x_train, y_train)

# figure out accuracy and confusion matrix based on simple model
y_pred = model.predict(x_test)
confusion_matrix(y_test, y_pred)

# start to fine tune model using various grid search parameters below
param_grid = [
              {'penalty': ['l1', 'l2'],
               'C': np.logspace(-4,4,20),
               'solver': ['liblinear']}
              ]

# launch grid search to find optimal variables
grid_search = GridSearchCV(model, param_grid, cv = 5, scoring='accuracy', n_jobs=-1)
grid_search.fit(x_train, y_train)

# initialise best model by calling the best estimator (i.e. combination of parameters from above) 
final_model = grid_search.best_estimator_

# look at results from the best model and how they compare to simple model
y_pred = final_model.predict(x_test)
print(classification_report(y_test,y_pred))
print("recall score", recall_score(y_test, y_pred))
print("f1_score", f1_score(y_test, y_pred))
print("precision", precision_score(y_test, y_pred))

# plot roc curve and confusion matrix to better visualise model performance 
sklearn.metrics.plot_roc_curve(final_model, x_test, y_test)
sklearn.metrics.plot_confusion_matrix(final_model, x_test, y_test, cmap='Blues')
