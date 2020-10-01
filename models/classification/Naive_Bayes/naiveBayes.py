
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,f1_score,roc_auc_score,recall_score,precision_score
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.model_selection import cross_val_score

#Read external data
Cad_train = pd.read_csv('./data/filtered_features/heart_train.csv')
Cad_test = pd.read_csv('./data/filtered_features/heart_test.csv')
#extract Xand Y

Y_train = Cad_train.CAD_Yes.values
Y_test = Cad_test.CAD_Yes.values

X_train = Cad_train.drop(['CAD_Yes'], axis = 1)
X_test = Cad_test.drop(['CAD_Yes'], axis = 1)


#Classifier Gaussian
Gaus_train = GaussianNB()
Gaus_train.fit(X_train, Y_train)

expected = Y_test
Gaus_predicted = Gaus_train.predict(X_test)
# summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, Gaus_predicted))


#binomial
binomial = BernoulliNB()
binomial.fit(X_train, Y_train)

binomial_predicted = binomial.predict(X_test)
# summarize the fit of the model
#print(metrics.classification_report(expected_test, predicted_test))
print(metrics.confusion_matrix(expected, binomial_predicted))

#binomial model accuracy
binomial.score(X_test, Y_test)

#cv 10
scores = cross_val_score(binomial, X_test, Y_test, cv=10, scoring="accuracy")
meanScore = scores.mean()
print(meanScore * 100)

multi = MultinomialNB()
multi.fit(X_train, Y_train)

expected =Y_test
predicted = multi.predict(X_test)
# summarize the fit of the model
#print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

multi.score(X_train, Y_train)

scores = cross_val_score(multi, X_test, Y_test, cv=10, scoring="accuracy")
meanScore = scores.mean()
print(scores)
print(meanScore * 100)


# Gaussian    : 71.4% (w/o cv) & 80.11% (with cv)
# Bernoulli   : 83.52% (w/o cv) & 84.89% (with cv)
# Multinomial : 58.24% (w/o cv) & 67% (with cv)