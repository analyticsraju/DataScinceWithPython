import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model, preprocessing
from sklearn import model_selection, metrics
import math

########################Data Preparation#########################
#Files: Concatenatio/Merging
def filesConcat(train, test):
    return pd.concat([train, test])
#Files: Splitting
def fileSplit(df, index):
    return (df[:index], df[index:])

#########PLOTTING/VISUALIZATION#######################################
#ContinuousVsCategorical
#def vizContVsCate(feature, target):
    
#ContinuousVsContinuous
#def vizContVsCont(feature, target):
    
    
#CategoricalVsCategorical
#def vizCateVsCate(feature, target):
    
#Continuous
#def vizCont(feature):
    
#Categorical
#def vizCate(feature):
    
#multiple graphs inside one graph
#def vizAllFeatureInOneGrid(features, target):

###########Feature Engineering###########################################
#Get Continuous columns
def getContinuousColumns(df):
    print("<=============all continuous columns===============>")
    return df.select_dtypes(include=['number']).columns

#Get Categorical columns
def getCategoricalColumns(df):
    print("<=============all categoric columns===============>")
    return df.select_dtypes(exclude=['number']).columns

#categorical=>continuous
#Ex: nuemeric categorical=>continuous
def transformCateToCont(df, features, mappings):
    for feature in features:
        null_idx = df[feature].isnull()
        df.loc[null_idx, feature] = None
        df[feature] = df[feature].map(mappings)
#continuous=>categorical
def transformContToCate(df, features):
    for feature in features:
        df[feature] = df[feature].astype('category')

#Filter Missing Data
def filterFeatures(df, features):
    df.drop(features, inplace=True, axis=1)

#def filterMissingDataFeatures(df, cutoff):
    #totalMissings = df


#Model Building
#Model: Fitting
#Model: Prediction


#Actual Coding Starts Here
os.chdir('D:/Data/DataScience/Practice/HousePrices/')

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.info()
#object means string
train.describe()
train.shape
test['SalePrice']=0
test.info()
#Merging two files train and test
all_houses = filesConcat(train, test)
train.info()
#object means string
train.describe()
train.shape
#Get All Continuous Columns
all_houses_cont_cols = getContinuousColumns(all_houses)
#Get All Categorical Columns
all_houses_cat_cols = getCategoricalColumns(all_houses)


all_houses.groupby('MSSubClass').size()

continus_column = ['MSSubClass']

#Converting to Continuous to Categorical
transformContToCate(all_houses, continus_column)

all_houses.info()

#after analysing(groupby) data, below columns are categorical columns and holding same kind of data.
#So I am Converting to Cate(String) to Continuous Data.
cat_columns = ["ExterQual", "ExterCond", "BsmtQual", "BsmtCond", "GarageQual", "GarageCond", "PoolQC", "FireplaceQu", "KitchenQual", "HeatingQC"]
mappings = {None: 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
transformCateToCont(all_houses, cat_columns, mappings)

all_houses['ExterQual']

print(getContinuousColumns(all_houses))
print(getCategoricalColumns(all_houses))

#SPLIT the data??????????
#Seems there is some columns have less data, that need to removed in train data.
#train_updtd, test_updtd = fileSplit(all_houses, train.shape[0])

#Filter missing data
total_missing_train = all_houses.isnull().sum()
n_train = train.shape[0]
to_delete_train = total_missing_train[(total_missing_train/n_train) > 1 ]#cutoff10%missing data
missingDataFeatures_train = list(to_delete_train.index)
all_houses.info()
#Droping missing data features from train data.
filterFeatures(all_houses,missingDataFeatures_train)

#Fill missing values
cont_features = getContinuousColumns(all_houses)
cat_features = getCategoricalColumns(all_houses)
    
mean_imputer = preprocessing.Imputer()
mean_imputer.fit(all_houses[cont_features])
all_houses[cont_features] = mean_imputer.transform(all_houses[cont_features])

#Here converting category(String) features to continuous feature takes more time. 
#Because here are columns
#MSZoning,Utilities,Exterior1st,Exterior2nd,MasVnrType,BsmtExposure,BsmtFinType1,BsmtFinType2,Electrical,Functional,GarageType,GarageFinish,SaleType
#Prepare Dictionary for each feature, and transforming takes more and more time
#Imputation not working for category(String) features. 
#mode_imputer = preprocessing.Imputer(strategy="most_frequent")
#mode_imputer.fit(all_houses[cat_features])
#all_houses[cat_features] = mode_imputer.transform(all_houses[cat_features])

#So. I am going to fill missing data with None type.
all_houses.fillna = None
all_houses.info()



#Explore relationship to Neighbourhood to SalePrice
plt.xticks(rotation=45)
sns.boxplot(x='Neighborhood', y='SalePrice',data=all_houses)

#Smooth the SalePrice using log transformation
all_houses['log_sale_price'] = np.log(all_houses['SalePrice'])
features = ['SalePrice', 'log_sale_price']
sns.distplot(all_houses['log_sale_price'],kde=False)

sns.jointplot(x = 'log_sale_price', y = 'SalePrice', data = all_houses)
all_houses.describe()
all_houses.info()

#explore all features continusous features vs SalePrice
corr = all_houses.select_dtypes(include=['number']).corr()
sns.heatmap(corr, square=True)
plt.xticks(rotation=70)
plt.yticks(rotation=70)

#explore relationship of livarea and totalbsmt to SalePrice
features = ['GrLivArea', 'TotalBsmtSF']
for feature in features:
    sns.jointplot(x=feature, y='SalePrice',data=all_houses)

all_houses.info()
filterFeatures(all_houses,['Id'])

#do one hot encoding
all_houses.info()
all_houses_onehot = pd.get_dummies(all_houses, getCategoricalColumns(all_houses))
all_houses_onehot.info()

train_updtd, test_updtd = fileSplit(all_houses_onehot, train.shape[0])

y_train=train_updtd['SalePrice']
filterFeatures(train_updtd, ['SalePrice','log_sale_price'])
X_train=train_updtd
X_train.info()


def rmse(y_orig, y_pred):
    return math.sqrt(metrics.mean_squared_error(y_orig,y_pred))

ridge_estimator = linear_model.Ridge(random_state=2017)
ridge_grid = {'alpha':[0.0,0.2,0.4,0.6,0.8,1.0]}
grid_ridge_estimator = model_selection.GridSearchCV(ridge_estimator,ridge_grid,scoring=metrics.make_scorer(rmse),cv=10)
grid_ridge_estimator.fit(X_train, y_train)
print(grid_ridge_estimator.grid_scores_)
print(grid_ridge_estimator.best_params_)
print(grid_ridge_estimator.best_score_)
print(grid_ridge_estimator.score(X_train, y_train))
estimator = grid_ridge_estimator.best_estimator_
estimator.coef_
estimator.intercept_

##################Final Prections Preparation

#total_missing_test = test_updtd.isnull().sum()
#n_test = test.shape[0]
#to_delete_test = total_missing_test[(total_missing_test/n_test) > 0 ]
#missingDataFeaturestes_test = list(to_delete_test.index)
#test_updtd.info()

#filterFeatures(test_updtd,missingDataFeatures_train)
#filterFeatures(test_updtd,['Id'])

#test_updtd.info()
#test_onehot = pd.get_dummies(test_updtd, getCategoricalColumns(test_updtd))
#test_onehot.info()
#filterFeatures(test_updtd, ['SalePrice'])

filterFeatures(test_updtd, ['SalePrice','log_sale_price'])
X_test = test_updtd
X_test.shape
X_test.info()
filterFeatures(test,['SalePrice'])

test['SalePrice'] = grid_ridge_estimator.predict(X_test)

test.to_csv('submission.csv', columns=['Id','SalePrice'],index=False)
print('<=====================Model Execution Completed===============>')
