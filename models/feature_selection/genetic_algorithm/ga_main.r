
############################################
# R script: ga_main.r
# Project: FIT3164 project
#
# Date: 03/09/2020
# Author: Tom Orlando with wrappers.r adapted
#         from 
# 
# Purpose: Building out genetic algorithm 
#          for feature selection   
############################################

rm(list = ls())
setwd("C:\\Users\\Tom Orlando\\Monash\\FIT3164")

#install.packages("caret")
#install.packages("randomForest")
#install.packages("funModeling")
#install.packages("tidyverse")
#install.packages("GA")
#install.packages("e1071")
#install.packages("doParallel")

library(caret)
library(randomForest)
library(funModeling)
library(tidyverse)
library(GA)
library("e1071")
source('./build/wrappers/ga_wrappers.R')

# Importing data with which we wish to find best features   
df <- read.csv('./data/full_data/heart_clean.csv')

# Preparing data to read into algorithm
df$CAD_Yes=factor(df$CAD_Yes,levels =c(0,1),labels = c('No','Yes'))   # required as ga function needs factors
df.y <- as.factor(df$CAD_Yes)
df.x <- select(df, -CAD_Yes)
num_vars <- ncol(df.x)
var_names <- colnames(df.x)

# Main function using the GA package and leveraging wrappers.r
ga_main <- ga(fitness = function(vars) custom_fitness(vars = vars,
                                                      data_x = df.x,
                                                      data_y = df.y,
                                                      p_sampling = 0.7),
                                                      
              type = "binary",
              crossover = gabin_uCrossover,
              elitism = 3,
              pmutation = 0.03,
              popSize = 50,
              nBits = num_vars,
              names = var_names,
              run = 5,
              maxiter = 50,
              monitor = plot,
              keepBest = TRUE,
              #parallel = TRUE,
              seed = 28009592
)

# Seeing the results of the algorithm with best features and tested with a random forest
summary(ga_main)
best_vars = var_names[ga_main@solution[1,]==1]
get_accuracy_metric(data_tr_sample = df.x, target = df.y, best_vars)



