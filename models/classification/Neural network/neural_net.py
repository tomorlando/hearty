import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import random
from sklearn.model_selection import cross_val_score

random.seed(100)

#Read external data
Cad_train = pd.read_csv('heart_train.csv')
Cad_test = pd.read_csv('heart_test.csv')

Y_train = Cad_train.CAD_Yes.values
Y_test = Cad_test.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)


#Neuralnet without scaling the data

MLP = MLPClassifier(hidden_layer_sizes=(11,10), max_iter = 500)
MLP.fit(X_train, Y_train)

pred = MLP.predict(X_test)
print(confusion_matrix(Y_test,pred))

#NN with scaled data

MLP2 = MLPClassifier(hidden_layer_sizes=(11,10), max_iter = 500)
scaler = MinMaxScaler(feature_range = (0,1))

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

MLP2.fit(X_train, Y_train)

pred2 = MLP2.predict(X_test)
print(confusion_matrix(Y_test,pred2))

scores = cross_val_score(MLP, X_train, Y_train, cv=10, scoring="accuracy")

meanScore = scores.mean()
print("mean score of decision tree is ",meanScore * 100)

scores = cross_val_score(MLP2, X_train, Y_train, cv=10, scoring="accuracy")

meanScore = scores.mean()
print("mean score of decision tree is ",meanScore * 100)


# Both scaled and not scaled produce above 80%