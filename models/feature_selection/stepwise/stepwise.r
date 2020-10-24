############################################
# File      : stepwise.r
# Project   : FIT3164 project
#
# Date      : 03/09/2020
# Author    : Abrar Fauzan Hamzah
# 
# Purpose   : Implementing stepwise to get 
#             important features and analyse
#             the AIC.
#             Lower AIC the better.
############################################

#import training set
x_train = read.csv('./data/heart_train.csv')

##BACKWARDS
#start with all features included as the predictors
fitAll <- lm(x_train$CAD_Yes ~., data = x_train)
#summary(fitAll)

step.back <- step(fitAll, direction = "backward")

# To get the formula uncomment the code below
# formula(step.back)

##FORWARD
fitStart <- lm(x_train$CAD_Yes ~ 1, data=x_train)
step.forward <- step(fitStart, direction="forward", scope=formula(fitAll))

# formula(step.forward)




