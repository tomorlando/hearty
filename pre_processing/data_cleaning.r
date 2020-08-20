

rm(list = ls())
setwd("C:\\Users\\Tom Orlando\\Monash\\FIT3164")

install.packages("readxl")
install.packages("dplyr")

library(readxl)
library("dplyr")

# load dataset and explore data 
heart <- read_excel('./data/initial_dataset.xlsx')
dim(heart)
summary(heart)
str(heart)
View(heart)

# Missing value processing -- if there is  null value,someone will be true
is.na(heart)
table(is.na(heart))
sum(is.na(heart))

# ALL N in exertional CP, not useful for this dataset to check if CAD
heart <- heart[,-which(colnames(heart) %in% c("Exertional CP"))]

# select all columns by datatypes
num <- select_if(heart, is.numeric)
chara <- select_if(heart, is.character)
summary(num)
summary(chara)

# Encoding categorical data
#encoding sex
heart$Sex=factor(heart$Sex,levels = c('Fmale','Male'),labels = c(0,1))
#encoding obesity
heart$Obesity=factor(heart$Obesity,levels = c('Y','N'),labels = c(1,0))
#encoding CRF
heart$CRF=factor(heart$CRF,levels = c('Y','N'),labels = c(1,0))
#encoding CVA
heart$CVA=factor(heart$CVA,levels = c('Y','N'),labels = c(1,0))
#encoding Airway disease
heart$`Airway disease`=factor(heart$`Airway disease`,levels =c('Y','N'),labels = c(1,0))
#encoding Thryoid Disease
heart$`Thyroid Disease`=factor(heart$`Thyroid Disease`,levels =c('Y','N'),labels = c(1,0))
#endoing CHF
heart$CHF=factor(heart$CHF,levels =c('Y','N'),labels = c(1,0))
#encoding DLP
heart$DLP=factor(heart$DLP,levels =c('Y','N'),labels = c(1,0))
#encoding Weak peripheral pulse
heart$`Weak Peripheral Pulse`=factor(heart$`Weak Peripheral Pulse`,levels =c('Y','N'),labels = c(1,0))
#encoding Lung rales
heart$`Lung rales`=factor(heart$`Lung rales`,levels =c('Y','N'),labels = c(1,0))
#encoding systolic murmur
heart$`Systolic Murmur`=factor(heart$`Systolic Murmur`,levels =c('Y','N'),labels = c(1,0))
#encoding  diastolic murmur
heart$`Diastolic Murmur`=factor(heart$`Diastolic Murmur`,levels =c('Y','N'),labels = c(1,0))
#encoding DYSPNEA
heart$Dyspnea=factor(heart$Dyspnea,levels =c('Y','N'),labels = c(1,0))
#encoding  ATYPICAL
heart$Atypical=factor(heart$Atypical,levels =c('Y','N'),labels = c(1,0))
#encoding nonanginal
heart$Nonanginal=factor(heart$Nonanginal,levels =c('Y','N'),labels = c(1,0))
#encoding lowth ang
heart$`LowTH Ang`=factor(heart$`LowTH Ang`,levels =c('Y','N'),labels = c(1,0))
#encoding LVH
heart$LVH=factor(heart$LVH,levels =c('Y','N'),labels = c(1,0))
#encoding poor r progression
heart$`Poor R Progression`=factor(heart$`Poor R Progression`,levels =c('Y','N'),labels = c(1,0))
#encoding BBB
heart$BBB=factor(heart$BBB,levels =c('LBBB','N','RBBB'),labels = c(0,1,2))
#encoding VHD
heart$VHD=factor(heart$VHD,levels =c('N','mild','Moderate','Severe'),labels = c(0,1,2,3))
#encoding Cath
heart$Cath=factor(heart$Cath,levels =c('Cad','Normal'),labels = c(1,0))

write.csv(heart,"heart.csv",row.names = FALSE)
nheart<- read.csv('./heart.csv')

str(nheart)