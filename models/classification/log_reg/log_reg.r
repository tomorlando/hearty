
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

# install.packages('pROC')
install.packages('boot')
library('boot')
library('pROC')
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

step.fit.bic <- step(model.fit, directoin = 'both', k=log(nrow(df.train)))
step.fit.aic <- step(model.fit, directoin = 'both')


my.pred.stats(predict(step.fit.aic, df.test, type='response'), df.test$CAD_Yes)