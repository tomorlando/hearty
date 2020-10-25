################################################
# File      : neural_net.py
# Project   : FIT3164 project
#
# Date      : 5/10/2020
# Author    : Abrar Fauzan Hamzah
# 
# Purpose: Implement Neural Network and tweak
#          the hyperparameters using GridSearch
#          & briefly analyse the performance   
###############################################

import numpy as np
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import random
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score
import pickle, joblib

#Read external data
Cad_train = pd.read_csv('./data/filtered_features/heart_train_std.csv')
Cad_test = pd.read_csv('./data/filtered_features/heart_test_std.csv')

Y_train = Cad_train.CAD_Yes.values
Y_test = Cad_test.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)

#Set of possibles parameter values 
nn_param = {
    'hidden_layer_sizes': [(2,),(5,),(5,2),(10,10),(11,10),(11,11)],
    'activation': ['relu','tanh'],
    'solver': ['sgd','adam'],
    'learning_rate': ['constant','adaptive']
}

from grid_search_wrapper import getBest_parameters

# initialise neural network
nn = MLPClassifier(max_iter=3000, random_state=42)

# Find the best parameter for neural network
best_param = getBest_parameters(nn, nn_param, X_train, Y_train)
# best parameters : {'activation': 'tanh', 'hidden_layer_sizes': (5,), 'learning_rate': 'constant', 'solver': 'adam'}

# Fit the model using the best set of parameters from GridSearch
best_nn = MLPClassifier(**best_param, max_iter=3000, random_state=42)
best_nn.fit(X_train,Y_train)

y_pred = best_nn.predict(X_test)

#Evaluating the Algorithm
print(confusion_matrix(Y_test,y_pred))
print(classification_report(Y_test,y_pred))
print("recall score",recall_score(Y_test, y_pred))
print("f1_score",f1_score(Y_test, y_pred))
print("precision",precision_score(Y_test, y_pred))
sklearn.metrics.plot_roc_curve(best_nn, X_test, Y_test)
sklearn.metrics.plot_confusion_matrix(best_nn, X_test, Y_test, cmap='Blues')
scores = cross_val_score(best_nn, X_train, Y_train, cv=10, scoring="accuracy")

meanScore = scores.mean()
print("mean score of decision tree is ",meanScore * 100)

#make pkl for neural network model
#joblib.dump(best_nn, 'dc_model.pkl')