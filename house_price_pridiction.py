# -*- coding: utf-8 -*-
"""House price pridiction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1csKt9GYdoTz6j39BtyzGkB8JdniQdpmW

Importing Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

"""Importing the boston house price data"""

house_price_data = sklearn.datasets.load_boston()
print(house_price_data)

# Loading the dataset to a pandas dataframe
house_price_dataframe = pd.DataFrame(house_price_data.data,columns =house_price_data.feature_names)

house_price_dataframe.head()

# adding the target(price) column to the dataframe
house_price_dataframe['price'] = house_price_data.target
house_price_dataframe.head()

# checking the no of rows and columns in the dataframe
house_price_dataframe.shape

# check for missing values
house_price_dataframe.isnull().sum()

# statisticals measures of the dataset
house_price_dataframe.describe()



"""Understanding the correlation between various feature in the dataset



1.   positive correlation(If one value of feature increases another feature value also increases)
2.   negative correlation(If one value of feature decreases another feature value also decreases)


"""

correlation = house_price_dataframe.corr()
#constructing a heapmap to understand the corelation
plt.figure(figsize=(10,10))
sns.heatmap(correlation , cbar =True, square = True , fmt = '.1f',annot = True ,annot_kws ={'size': 8},cmap='Blues')

"""spliting the data & target"""

# dropping a particular column
x = house_price_dataframe.drop(['price'],axis =1)
y = house_price_dataframe['price']
print(x)
print(y)

"""spliting the data into training data and test data"""

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size =0.2,random_state=2)

print(x.shape,x_train.shape,x_test.shape)

"""Model Training

XGBoost Regressor
"""

#loading the model 
model = XGBRegressor()

# training the model with x_train
model.fit(x_train,y_train)

"""Evaluation
prediction on training data
"""

# accuracy for prediction on training data
training_data_prediction = model.predict(x_train)

print(training_data_prediction)

# R squared error training data
score_1 = metrics.r2_score(y_train,training_data_prediction)

#mean absolute error
score_2 = metrics.mean_absolute_error(y_train,training_data_prediction)

print("R squared error : " ,score_1)
print("Mean absolute error : ",score_2)

"""visualizing the actual prices and predicted prices"""

plt.scatter(y_train, training_data_prediction)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

"""prediction on tesing data"""

# accuracy for prediction on tesing data
testing_data_prediction = model.predict(x_test)

# R squared error for tesing data
score_1 = metrics.r2_score(y_test,testing_data_prediction)

# mean absolute error
score_2 = metrics.mean_absolute_error(y_test,testing_data_prediction)

print("R squared error for testing data : " ,score_1)
print("Mean absolute error for testing data : ",score_2)

