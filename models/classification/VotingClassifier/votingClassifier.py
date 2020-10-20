
import pandas as pd
import numpy as np, random
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
import pickle
import joblib


#Reading the data
Cad_train = pd.read_csv('./data/filtered_features/heart_train_std.csv')
Cad_test = pd.read_csv('./data/filtered_features/heart_test_std.csv')

#Get x & y values
Y_train = Cad_train.CAD_Yes.values
Y_test = Cad_test.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)


# initialise list of estimators
estimator = []

# The code chunk below is fitting the model which uses the best parameters after gridSearchCV
best_nn = MLPClassifier(max_iter=3000, activation='tanh', hidden_layer_sizes=(5,), learning_rate='constant', solver='adam')
best_nn.fit(X_train,Y_train)

best_lr = LogisticRegression(C=4.281332398719396, penalty='l1', solver='liblinear')
best_lr.fit(X_train,Y_train)


SVM = SVC(probability=True)
svc_param_grid = {'kernel': ['rbf','linear'],
                  'gamma': [ 0.001, 0.01, 0.1, 1],
                  'C': [1, 10, 50, 100,200,300, 1000]}

from grid_search_wrapper import getBest_parameters

best_param = getBest_parameters(SVM, svc_param_grid, X_train, Y_train)
best_svm = SVC(**best_param, probability=True)
best_svm.fit(X_train,Y_train)

DT = DecisionTreeClassifier()

dt_param_grid = {'criterion': ['gini','entropy'],
                 'max_depth': range(1,10)
                 }

best_dt_param = getBest_parameters(DT, dt_param_grid, X_train, Y_train)
best_dt = DecisionTreeClassifier(**best_dt_param)
best_dt.fit(X_train,Y_train)



NB = BernoulliNB()
nb_param_grid = { 'alpha': [0.01,0.1,0.5,1,10]
                }
best_param_nb = getBest_parameters(NB, nb_param_grid, X_train, Y_train)
best_nb = BernoulliNB(**best_param_nb)
best_nb.fit(X_train,Y_train)

#append all estimators to the list
estimator.append(('DTC', best_dt))
estimator.append(('NN', best_nn))
estimator.append(('LR', best_lr))
estimator.append(('SVC', best_svm))
estimator.append(('NB', best_nb))

''''''
final_model = VotingClassifier(estimators=estimator, voting='soft')
final_model.fit(X_train, Y_train)


# soft voting = take the average/mean value
# hard voting = take the majority output
    ## cannot use predict_proba when using Hard voting

y_pred = final_model.predict(X_test)

score = accuracy_score(Y_test, y_pred)
print(score)

print(confusion_matrix(Y_test,y_pred))

#TODO add in more metrics
scores = cross_val_score(final_model, X_train, Y_train, cv=5, scoring="accuracy")
meanScore = scores.mean()
print("mean score of final model is ", meanScore * 100)

#joblib.dump(final_model, 'final_model.pkl')

