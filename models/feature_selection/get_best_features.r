

df <- read.csv('./data/full_data/heart_clean.csv')

# Adding in new features based on frequency count 
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

# Splitting into training and testing set
set.seed(28009592)
train.row <- sample(1:nrow(df.filt), 0.7*nrow(df.filt))
df.train <- df.filt[train.row,]
df.test <- df.filt[-train.row,]

# Saving to new files 
write.csv(df.train, './data/filtered_features/heart_train.csv', row.names = FALSE)
write.csv(df.test, './data/filtered_features/heart_test.csv', row.names = FALSE)