############################################
# File      : get_best_features.r
# Project   : FIT3164 project
#
# Date      : 03/09/2020
# Author    : Abrar Fauzan Hamzah
# 
# Purpose   : Filtering all the best features 
#             based on output from feature selection 
#             algorithms.
############################################

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