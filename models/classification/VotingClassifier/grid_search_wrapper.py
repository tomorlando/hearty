############################################
# File      : grid_search_wrapper.py
# Project   : FIT3164 project
#
# Date      : 5/10/2020
# Author    : Abrar Fauzan Hamzah
# 
# Purpose: Building a function to get the 
#          best set of parameters for a model   
############################################


from sklearn.model_selection import GridSearchCV

def getBest_parameters(model, param_grid, X_train, Y_train):
    '''
    Function to get the best hyperparameters

    Parameters
    ----------
    param_grid : set of possible parameters
    model: the estimator
    X_train: training data
    Y_train: the output training data

    return: best set of hyperparameters
    '''
    #perform a grid search and use cv=5, n-jobs means use all processor to run
    grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    grid_search.fit(X_train, Y_train)

    #get the best set of parameters of the model
    best_param = grid_search.best_params_

    return best_param