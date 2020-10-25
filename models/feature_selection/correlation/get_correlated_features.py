############################################
# File      : get_correlated_features.py
# Project   : FIT3164 project
#
# Date      : 03/09/2020
# Author    : Abrar Fauzan Hamzah
# 
# Purpose   : Building a function to get the 
#             correlated features which will
#             be dropped from the dataset   
############################################

def get_corr_features(data, threshold):
    '''
    Author      : Abrar Fauzan Hamzah
    Purpose     : Function to get correlated features
    data        : CAD dataset
    threshold   : a number (0-1) that used to determine to add features or not
    return      : set of correlated features
    '''
    #initialise the set
    corr_col = set()

    #create correlation matrix
    corrmat = data.corr()

    #this loop will iterate all features
    for i in range(len(corrmat.columns)):
        for j in range(i):
            #for two features, if correlation > threshold then add to set
            if abs(corrmat.iloc[i,j])> threshold:
                colname = corrmat.columns[i]
                corr_col.add(colname)
            
    return corr_col