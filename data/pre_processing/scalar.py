import pandas as pd
from sklearn.preprocessing import MinMaxScaler
#Read external data
df = pd.read_csv(r'C:\Users\tanji\Desktop\FIT3164\data\full_data\heart_train_nf.csv')
y_train = df.CAD_Yes.values
x_train = df.drop(['CAD_Yes'], axis=1)
df_test = pd.read_csv(r'C:\Users\tanji\Desktop\FIT3164\data\full_data\heart_test_nf.csv')
y_test = df_test.CAD_Yes.values
x_test = df_test.drop(['CAD_Yes'], axis=1)
#scalar

scaler = MinMaxScaler(feature_range = (0,1))

scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

df=df[['typical_chest_pain','Age','DM','HTN','FH','TG','K','region_rwma','BBBN','Tinversion','FBS','ESR','EF.TTE','DLPY','diastolic_murmurY','CAD_Yes']]
df_test=df_test[['typical_chest_pain','Age','DM','HTN','FH','TG','K','region_rwma','BBBN','Tinversion','FBS','ESR','EF.TTE','DLPY','diastolic_murmurY','CAD_Yes']]

df.to_csv("C:/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_train_new.csv", index=False)
df_test.to_csv("C:/Users/tanji/Desktop/FIT3164/data/filtered_features/heart_test_new.csv", index=False)