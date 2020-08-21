
############################################
# R script: lasso_fs.r
# Project: FIT3164 project
#
# Date: 21/08/2020
# Author: Tom Orlando
# 
# Purpose: Code to build out lasso feature
#          selection algorithm 
############################################

rm(list = ls())
setwd("C:\\Users\\Tom Orlando\\Monash\\FIT3164")

#install.packages("glmnet")
library(glmnet)
source('./models/feature_selection/lasso/wrappers.R')
source("./models/feature_selection/lasso/my_pred_stats.R")

# Importing training dataset of which we will find  
df <- read.csv('./data/heart_train.csv')

# Using lasso to penalise (and filter) non-important variables with various lambdas
lasso.fit <- glmnet.f(CAD_Yes~., df, family='binomial', lambda = 0.02)
coefficients(lasso.fit)
sum(coefficients(lasso.fit) != 0)

lasso.fit <- glmnet.f(CAD_Yes~., df, family='binomial', lambda = 0.05)
coefficients(lasso.fit)
sum(coefficients(lasso.fit) != 0)

lasso.fit <- glmnet.f(CAD_Yes~., df, family='binomial', lambda = 0.03)
coefficients(lasso.fit)
sum(coefficients(lasso.fit) != 0)

# We can plot the coefficient paths, to indicate which features are least important
lasso.fit <- glmnet.f(CAD_Yes~., df, family = 'binomial')
plot(lasso.fit, 'lambda', label=T)

# Using cross-validation to find optimal lambda value
lambda.cv <- cv.glmnet.f(CAD_Yes~., df, family = 'binomial')
plot(lambda.cv)
min(lambda.cv$cvm)

# Fitting our new lasso feature selector with best lambda value and testing
lasso.fit <- glmnet.f(CAD_Yes~., df, family='binomial', lambda = lambda.cv$lambda.min)
coefficients(lasso.fit)
sum(coefficients(lasso.fit) != 0)

df.test <- read.csv('./data/heart_test.csv')
my.pred.stats(predict.glmnet.f(lasso.fit, df.test, type='response'), df.test$CAD_Yes)