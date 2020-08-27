
x_train = read.csv('./data/heart_train.csv')

##BACKWARDS
#start with all features included as the predictors
fitAll <- lm(x_train$CAD_Yes ~., data = x_train)
#summary(fitAll)

step.back <- step(fitAll, direction = "backward")
#formula(step.back)

#'Age', 'Weight', 'Length', 'BMI', 'DM', 'HTN', 'FH', 'PR', 'typical_chest_pain', 'Tinversion', 'FBS', 'TG', 'BUN', 'ESR', 'K', 'Na', 'WBC', 'EF.TTE', 'region_rwma', 'SexMale', 'DLPY', 'lung_ralesY', 'diastolic_murmurY', 'lowth_angY', 'LVHY', 'BBBN', 'VHDModerate'

    # AIC = -477.19
    # 27 features selected

##FORWARD

fitStart <- lm(x_train$CAD_Yes ~ 1, data=x_train)
#step.forward <- step(fitStart, direction="forward", scope=formula(fitAll))

#'typical_chest_pain', 'region_rwma', 'HTN', 'Age', 'FBS', 'TG' ,'FH' , 'EF.TTE' , 'BBBN', 'DLPY', 'diastolic_murmurY', 'K', 'Tinversion', 'DM'

    #AIC: -476.17
    #14 Features




