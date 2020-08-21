

# wrapper for glmnet
glmnet.f <- function(formula, data, ...)
{
  # Make sure the outcome variable is the first column
  mf = model.frame(formula = formula, data = data)
  t = terms.formula(formula, data=data)
  
  # get the outcome
  y = as.matrix(mf[,1])
  
  # get the predictors and remove the intercept column
  X = model.matrix(t, data=mf)
  X = X[,-1]   
  
  fit <- glmnet(X, y, ...)
  fit$formula <- formula
  
  return(fit)
}

# wrapper for cv.glmnet
cv.glmnet.f <- function(formula, data, ...)
{
  # Make sure the outcome variable is the first column
  mf = model.frame(formula = formula, data = data)
  t = terms.formula(formula, data=data)
  
  # get the outcome
  y = as.matrix(mf[,1])
  
  # get the predictors and remove the intercept column
  X = model.matrix(t, data=mf)
  X = X[,-1]   
  
  fit <- cv.glmnet(X, y, ...)
  fit$formula <- formula
  
  return(fit)
}

# wrapper for predict.glmnet
predict.glmnet.f <- function(fit, data, ...) {
  
  # Make sure the outcome variable is the first column
  mf = model.frame(formula = fit$formula, data = data)
  t = terms.formula(fit$formula,data=data)
  
  # get the predictors and remove the intercept column
  #X = model.matrix(t, data=mf)
  #X = X[,-1]   
  
  yhat <- predict(fit, X,  ...)
  
  return(yhat)
}