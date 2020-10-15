import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import random
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV


#Read external data
Cad_train = pd.read_csv('heart_train_std.csv')
Cad_test = pd.read_csv('heart_test_std.csv')

Y_train = Cad_train.CAD_Yes.values
Y_test = Cad_test.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)


nn_param = {
    'hidden_layer_sizes': [(2,),(5,),(5,2),(10,10),(11,10),(11,11)],
    'activation': ['relu','tanh'],
    'solver': ['sgd','adam'],
    'learning_rate': ['constant','adaptive']
}

from grid_search_wrapper.py import getBest_parameters()

nn = MLPClassifier(max_iter=3000, random_state=42)

best_param = getBest_parameters(nn, nn_param, X_train, Y_train)
# best parameters : {'activation': 'tanh', 'hidden_layer_sizes': (5,), 'learning_rate': 'constant', 'solver': 'adam'}


yyy = MLPClassifier(**best_param, max_iter=3000, random_state=42)
yyy.fit(X_train,Y_train)

nn_y = yyy.predict(X_test)
print(confusion_matrix(Y_test,nn_y))