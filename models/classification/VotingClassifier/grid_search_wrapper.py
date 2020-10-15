'''
Function to get the best hyperparameters
param_grid : set of possible parameters
model: the estimator
X_train: training data
Y_train: the output training data
return: best set of hyperparameters
'''
from sklearn.model_selection import GridSearchCV

def getBest_parameters(model, param_grid, X_train, Y_train):
    grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1, scoring='accuracy')
    grid_search.fit(X_train, Y_train)

    #get the estimator using the best hyperparameters
    best_param = grid_search.best_params_

    return best_param