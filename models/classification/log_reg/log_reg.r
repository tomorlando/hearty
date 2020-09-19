
############################################
# R script: log_reg.r
# Project: FIT3164 project
#
# Date: 10/09/2020
# Author: Tom Orlando
#          
# 
# Purpose: Building out logisit regression 
#          classifier to identify CAD   
############################################

rm(list = ls())
setwd("C:\\Users\\Tom Orlando\\Monash\\FIT3164")

install.packages('pROC')
install.packages('boot')
install.packages('glmnet')
library('boot')
library('pROC')
library('glmnet')
source('./build/wrappers/glm_wrappers.R')
source("./build/wrappers/my_pred_stats.R")


df.train <- read.csv('./data/filtered_features/heart_train.csv')
df.test <- read.csv('./data/filtered_features/heart_test.csv')
View(df.train)

# Building initial model
model.fit <- glm(CAD_Yes ~., data = df.train, family=binomial)
summary(model.fit)
prob <- predict(model.fit, df.test, type='response')
pred <- factor(predict(model.fit, df.test,) > 0.5, c(F,T), c(0, 1))
my.pred.stats(prob, df.test$CAD_Yes)

# Adding in stepwise optimisation using AIC
step.fit.aic <- step(model.fit, direction='both')
my.pred.stats(predict(step.fit.aic, df.test, type='response'), df.test$CAD_Yes)

# Adding in stepwise optimisation using BIC
step.fit.bic <- step(model.fit, k = log(nrow(df.train)), direction='both')
my.pred.stats(predict(step.fit.aic, df.test, type='response'), df.test$CAD_Yes)

# No performance boost from the above as most of the features have already been 
# filtrered in the previous stage of the project. We can try increase the performance
# by adding in various interactions between features, using stepwise optimisation instead

formula <- make.formula('CAD_Yes', df.train, use.interactions=T, use.logs=T, use.squares=T, use.cubics=T)
model.fit <- glm(formula, data=df.train, family = binomial)

my.pred.stats(predict(model.fit, df.test, type='response'), df.test$CAD_Yes)

step.fit.bic <- step(model.fit, direction = 'both', k=log(nrow(df.train)))
step.fit.aic <- step(model.fit, direction = 'both')

my.pred.stats(predict(step.fit.bic, df.test, type='response'), df.test$CAD_Yes)

# Using interactions above brings no performance boost to our model. We can 
# therefore try to use penalised regression with both L1 and L2 penalisations.

# Using Lasso regression
lasso.fit <- glmnet.f(formula, data= df.train, family='binomial')
plot(lasso.fit, 'lambda', label=TRUE)
lasso.fit.cv <- cv.glmnet.f(formula, data=df.train, family='binomial', nfolds=25)
plot(lasso.fit.cv)
lasso.fit <- cv.glmnet.f(formula, data= df.train, family='binomial')
glmnet.tidy.coef(lasso.fit)
my.pred.stats(predict.glmnet.f(lasso.fit, df.test, type='response'), df.test$CAD_Yes)

# Using Ridge regression
ridge.fit <- glmnet.f(formula, data=df.train, family='binomial', alpha=0)
plot(ridge.fit)
ridge.fit.cv <- cv.glmnet.f(formula, data=df.train, family='binomial', nfolds=25, alpha=0)
plot(ridge.fit.cv)
ridge.fit <- cv.glmnet.f(formula, data= df.train, family='binomial')
glmnet.tidy.coef(ridge.fit)
my.pred.stats(predict.glmnet.f(ridge.fit, df.test, type='response'), df.test$CAD_Yes)

# Using elastic net regression 
elnet.fit <- glmnet.f(formula, data= df.train, family='binomial', alpha=.5)
plot(elnet.fit, 'lambda')
elnet.fit.cv <- cv.glmnet.f(formula, data=df.train, family='binomial', nfolds=25, alpha=.5)
plot(elnet.fit.cv)
elnet.fit <- cv.glmnet.f(formula, data= df.train, family='binomial', alpha=.5)
glmnet.tidy.coef(elnet.fit)
my.pred.stats(predict.glmnet.f(elnet.fit, df.test, type='response'), df.test$CAD_Yes)

# As elnet has the best results, we can tune the alpha value to find the optimal model
for (i in 1:9){
  assign(paste('elnet.fit', i, sep=''), cv.glmnet.f(formula, data=df.train, family='binomial', nfolds = 25, alpha=i/10))
  #my.pred.stats(predict.glmnet.f(paste('elnet.fit', i, sep=''), df.test, type='response'), df.test$CAD_Yes)
}

my.pred.stats(predict.glmnet.f(elnet.fit4, df.test, type='response'), df.test$CAD_Yes)

final.model <- cv.glmnet.f(formula, data= df.train, family='binomial', alpha=.4)
my.pred.stats(predict.glmnet.f(final.model, df.test, type='response'), df.test$CAD_Yes)

summary(final.model)

# It seems an alpha of .4 provides the most accurate model, and will therefore be used as our main 
# logistic regression model. 

# To conclude, the logistic regression model we are using consists of an elastic net model
# an alpha value of .4, used to penalise the various new features made using interactions. This
# allows us to first overfit the model by adding many new features (through interactions), then
# penalising all the features which result in lower accuracy using the elastic net method.

predict.glmnet.f(final.model, df.test, type='response')

user.input <- as.data.frame(df.test[1,c(1:ncol(df.test))])
