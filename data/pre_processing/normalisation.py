import pandas as pd
from sklearn.preprocessing import MinMaxScaler

heart_train = pd.read_csv('heart_train.csv')
heart_test = pd.read_csv('heart_test.csv')

heart_train_norm = heart_train
heart_test_norm = heart_test

Y_train = heart_train.CAD_Yes.values
Y_test = heart_test.CAD_Yes.values

X_train = heart_train.drop(['CAD_Yes'], axis = 1)
X_test = heart_test.drop(['CAD_Yes'], axis = 1)

#scale the data
scaler = MinMaxScaler(feature_range = (0,1))
scaler.fit(X_train)

X_train_norm = scaler.transform(X_train)
X_test_norm = scaler.transform(X_test)

#convert into dataframe
X_train2 = pd.DataFrame(X_train_norm, columns=X_train.columns)
X_test2 = pd.DataFrame(X_test_norm, columns=X_test.columns)

X_train2['CAD_Yes'] = Y_train
X_test2['CAD_Yes'] = Y_test

#make new file for normalised data
X_train2.to_csv(r'./data/filtered_features/heart_train_std.csv', index = False)
X_test2.to_csv(r'./data/filtered_features/heart_test_std.csv', index = False)

