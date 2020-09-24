rm(list=ls())

library(neuralnet)
library(caret)


set.seed(100)

Cad_train = read.csv('./data/filtered_features/heart_train.csv')
Cad_test = read.csv('./data/filtered_features/heart_test.csv')

#build the model
nn = neuralnet(CAD_Yes~.,data = Cad_train, hidden = 5,linear.output = FALSE)
###linear output is FALSE since we are dealing with categorical output feature (0 if no CAD, 1 if yes)

#plot(nn)
#nn$result.matrix

#predict the test dataset
nn.results <- compute(nn, Cad_test)
results <- data.frame(actual = Cad_test$CAD_Yes, prediction = nn.results$net.result)

#create confusion matrix
roundedresults<-sapply(results,round,digits=0)
roundedresultsdf=data.frame(roundedresults)
attach(roundedresultsdf)
table(actual,prediction)

# 2 Hidden layers : Accuracy = 14+57 / (14+57+8+12)
#                          = 0.78

# 5 Hidden layers : Accuracy = 14+64 / (14+64+8+5)
#                          = 0.857

