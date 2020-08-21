
rm(list = ls())

# setwd("C:\\Users\\Tom Orlando\\Monash\\FIT3164")

# install.packages("readxl")
# install.packages("dplyr")

library(readxl)
library("dplyr")

# load dataset and explore data 
heart <- read_excel('./data/full_data/heart_initial.xlsx')
dim(heart)
summary(heart)
str(heart)

# Missing value processing -- if there is  null value,someone will be true
table(is.na(heart))
sum(is.na(heart))

# ALL N in exertional CP, not useful for this dataset to check if CAD
heart <- heart[,-which(colnames(heart) %in% c("Exertional CP"))]

# select all columns by datatypes
num <- select_if(heart, is.numeric)
chara <- select_if(heart, is.character)
summary(num)

# Renaming columns with spaces
df <- as_tibble(heart)

df <- df %>% rename(
    airway_disease = `Airway disease`,
    thyroid_disease = `Thyroid Disease`,
    weak_periph_pulse = `Weak Peripheral Pulse`,
    lung_rales = `Lung rales`,
    systolic_murmur = `Systolic Murmur`,
    diastolic_murmur = `Diastolic Murmur`,
    lowth_ang = `LowTH Ang`,
    poor_r_progression = `Poor R Progression`,
    current_smoker = `Current Smoker`,
    typical_chest_pain = `Typical Chest Pain`,
    function_class = `Function Class`,
    q_wave = `Q Wave`,
    st_elevation = `St Elevation`,
    st_depression = `St Depression`,
    region_rwma = `Region RWMA`
  )

# Encoding categorical data
df.mm <- model.matrix(~Sex+Obesity+CRF+CVA+airway_disease+thyroid_disease+CHF+DLP+weak_periph_pulse+
                          lung_rales+systolic_murmur+diastolic_murmur+Dyspnea+Atypical+Nonanginal+
                          lowth_ang+LVH+poor_r_progression+BBB+VHD, data = df)
df.mm <- df.mm[,-1] # removing "(intercept) column"

# Delete all previous non-encoded version of categorical columns
df <- df[, -which(colnames(df) %in% c("Sex", "Obesity", "CRF", "CVA", "airway_disease","thyroid_disease","CHF","DLP","weak_periph_pulse",
                          "lung_rales","systolic_murmur","diastolic_murmur","Dyspnea","Atypical","Nonanginal",
                          "lowth_ang","LVH","poor_r_progression","BBB","VHD"))]

# Combine dummy variables with initial columns 
df.combined <- cbind(df, df.mm)
df.combined$CAD_Yes=factor(df.combined$Cath,levels =c('Cad','Normal'),labels = c(1,0))
df.combined <- df.combined[, -which(colnames(df.combined) %in% c("Cath"))]

View(df.combined)

# Save down file to a new csv
write.csv(df.combined,"./data/full_data/heart_clean.csv", row.names = FALSE)
nheart<- read.csv('./data/full_data/heart_clean.csv')

View(nheart)
# splitting data into training and test set
set.seed(28009592)
train.row <- sample(1:nrow(nheart), 0.7*nrow(nheart))
df.train <- nheart[train.row,]
df.test <- nheart[-train.row,]

nrow(df.train)
nrow(df.test)
nrow(nheart)

write.csv(df.train, './data/heart_train.csv', row.names = FALSE)
write.csv(df.test, './data/heart_test.csv', row.names = FALSE)