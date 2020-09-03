

df <- read.csv('./data/full_data/heart_clean.csv')

df.filt <- df[, c('typical_chest_pain', 'Age',
'DM',
'HTN',
'FH',
'TG',
'K',
'region_rwma',
'BBBN',
'Tinversion',
'FBS',
'ESR',
'EF.TTE',
'DLPY',
'diastolic_murmurY', 
'CAD_Yes')]

set.seed(28009592)
train.row <- sample(1:nrow(df.filt), 0.7*nrow(df.filt))
df.train <- df.filt[train.row,]
df.test <- df.filt[-train.row,]

nrow(df.train)
nrow(df.test)
nrow(df.filt)

write.csv(df.train, './data/filtered_features/heart_train.csv', row.names = FALSE)
write.csv(df.test, './data/filtered_features/heart_test.csv', row.names = FALSE)