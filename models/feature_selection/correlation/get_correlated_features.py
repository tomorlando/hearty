#create functions to remove/add features based on correlation by the threshold
def get_corr_features(data, threshold):
    corr_col = set()
    corrmat = data.corr()
    #this loop will iterate all features
    for i in range(len(corrmat.columns)):
        for j in range(i):
            if abs(corrmat.iloc[i,j])> threshold:
                colname = corrmat.columns[i]
                corr_col.add(colname)
            
    return corr_col