import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load the full, train and test data
fulldata = pd.read_csv('./data/full_data/heart_clean.csv')
heart_train = pd.read_csv('./data/heart_train.csv')
heart_test = pd.read_csv('./data/heart_test.csv')

#drop the target variable
x_train = heart_train.drop('CAD_Yes', axis=1)
x_test = heart_test.drop('CAD_Yes', axis=1)
y = fulldata['CAD_Yes']

#plot a heatmap to get a general view of the correlation of the features
corr = x_train.corr()
plt.figure(figsize=(17,6))
sns.heatmap(corr)

from get_correlated_features import get_corr_features

#get all correlated features to be dropped
corr_features = get_corr_features(x_train, 0.3)
##corr_features

X_train_uncorr = x_train.drop(labels=corr_features, axis=1)
X_test_uncorr = x_test.drop(labels=corr_features, axis=1)

X_train_uncorr.shape, X_test_uncorr.shape