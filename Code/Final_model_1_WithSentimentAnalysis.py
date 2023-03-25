# -*- coding: utf-8 -*-
"""Copy of Final model 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yUVD2ReZ8f69zvvpebna9qNDa8aWKQj5
"""

#importing libraries
import warnings
warnings.filterwarnings('ignore')
 
import math
import pandas as pd
import numpy as npp

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
 
import matplotlib.pyplot as plt
import seaborn as sns
 
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Dense, Activation
 
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
 
from sklearn import preprocessing, metrics
from sklearn.preprocessing import MinMaxScaler
for i in ['gutenberg','punkt','vader_lexicon']:              
  nltk.download(str(i))
from nltk.sentiment.vader import SentimentIntensityAnalyzer as vader
print('Libraries Imported')

! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

stock_price=pd.read_csv('/content/NEWS_YAHOO_stock_prediction (1).csv')
stock_price

ohe = OneHotEncoder()
ohe.fit_transform(stock_price[["category"]]).toarray()
feature_arry = ohe.fit_transform(stock_price[["category"]]).toarray()
print(feature_arry)

ohe.categories_

feature_labels = ohe.categories_
np.array(feature_labels).ravel()
feature_labels = np.array(feature_labels).ravel()
print(feature_labels)

features = pd.DataFrame(feature_arry, columns = feature_labels)

stock_price = pd.concat([stock_price, features], axis=1)

stock_price.columns

# dropping duplicates
stock_price = stock_price.drop_duplicates()

# coverting the datatype of column 'Date' from type object to type 'datetime'
stock_price['Date'] = pd.to_datetime(stock_price['Date']).dt.normalize()

# filtering the important columns required
stock_price = stock_price.filter([ 'Date', 'category', 'title', 'content', 'Open',
       'High', 'Low', 'Close', 'Volume', 'label', 'news',
       'opinion'])

# setting column 'Date' as the index column
stock_price.set_index('Date', inplace= True)

# sorting the data according to the index i.e 'Date'
stock_price = stock_price.sort_index(ascending=True, axis=0)
stock_price

stock_price['compound_tit'] = ''
stock_price['negative_tit'] = ''
stock_price['neutral_tit'] = ''
stock_price['positive_tit'] = ''
stock_price['compound_con'] = ''
stock_price['negative_con'] = ''
stock_price['neutral_con'] = ''
stock_price['positive_con'] = ''
stock_price.head()

stock_price.columns

# importing requires libraries to analyze the sentiments
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata

# instantiating the Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# calculating sentiment scores
stock_price['compound_tit'] = stock_price['title'].apply(lambda x: sid.polarity_scores(x)['compound'])
stock_price['negative_tit'] = stock_price['title'].apply(lambda x: sid.polarity_scores(x)['neg'])
stock_price['neutral_tit'] = stock_price['title'].apply(lambda x: sid.polarity_scores(x)['neu'])
stock_price['positive_tit'] = stock_price['title'].apply(lambda x: sid.polarity_scores(x)['pos'])

stock_price['compound_con'] = stock_price['content'].apply(lambda x: sid.polarity_scores(x)['compound'])
stock_price['negative_con'] = stock_price['content'].apply(lambda x: sid.polarity_scores(x)['neg'])
stock_price['neutral_con'] = stock_price['content'].apply(lambda x: sid.polarity_scores(x)['neu'])
stock_price['positive_con'] = stock_price['content'].apply(lambda x: sid.polarity_scores(x)['pos'])
# displaying the stock data
stock_price.head()

stock_price.columns

# dropping the 'headline_text' which is unwanted now
stock_price.drop(['title','content','category'], inplace=True, axis=1)


# displaying the final stock_data
stock_price.head()

from pandas_profiling import ProfileReport
#We only use the first 10000 data points
prof = ProfileReport(stock_price) 
prof.to_file(output_file='output.html')

prof.to_notebook_iframe()

# setting figure size
plt.figure(figsize=(16,10))

# plotting close price
stock_price['Close'].plot()

# setting plot title, x and y labels
plt.title("Close Price")
plt.xlabel('Date')
plt.ylabel('Close Price ($)')

# calculating 7 day rolling mean
stock_price.rolling(7).mean().head(20)

# setting figure size
plt.figure(figsize=(16,10))

# plotting the close price and a 30-day rolling mean of close price
stock_price['Close'].plot()
stock_price.rolling(window=30).mean()['Close'].plot()

# calculating data_to_use
percentage_of_data = 1.0
data_to_use = int(percentage_of_data*(len(stock_price)-1))

# using 80% of data for training
train_end = int(data_to_use*0.8)
total_data = len(stock_price)
start = total_data - data_to_use

# printing number of records in the training and test datasets
print("Number of records in Training Data:", train_end)
print("Number of records in Test Data:", total_data - train_end)

stock_price.columns

# predicting one step ahead
steps_to_predict = 1

# capturing data to be used for each column
open_price = stock_price.iloc[start:total_data,0] #open
high = stock_price.iloc[start:total_data,1] #high
low = stock_price.iloc[start:total_data,2] #low
close_price = stock_price.iloc[start:total_data,3] #close
volume = stock_price.iloc[start:total_data,4] #volume
label = stock_price.iloc[start:total_data,5] #label
news = stock_price.iloc[start:total_data,6] #news
opinion = stock_price.iloc[start:total_data,7] #opinion
compound_tit = stock_price.iloc[start:total_data,8] #compound_tit
negative_tit = stock_price.iloc[start:total_data,9] #neg_tit
neutral_tit = stock_price.iloc[start:total_data,10] #neu_tit
positive_tit = stock_price.iloc[start:total_data,11] #pos_tit
compound_con=stock_price.iloc[start:total_data,12]#compound_con
negative_con=stock_price.iloc[start:total_data,13]#neg_con
neutral_con=stock_price.iloc[start:total_data,14]#neu_con
positive_con=stock_price.iloc[start:total_data,15]#pos_con

# printing close price
print("Close Price:")
close_price

# shifting next day close
close_price_shifted = close_price.shift(-1) 

# shifting next day compound
compound_shifted_con = compound_con.shift(-1) 

compound_shifted_tit = compound_tit.shift(-1) 

# concatenating the captured training data into a dataframe
data = pd.concat([close_price, close_price_shifted, compound_con, compound_shifted_con,compound_shifted_tit,compound_tit, volume, open_price, high, low], axis=1)

# setting column names of the revised stock data
data.columns = ['close_price', 'close_price_shifted', 'compound_con', 'compound_shifted_con','compound_shifted_tit','compound_tit','volume', 'open_price', 'high', 'low']

# dropping nulls
data = data.dropna()    
data.head(10)

# setting the target variable as the shifted close_price
y = data['close_price_shifted']
y

# setting the features dataset for prediction  
cols = ['close_price', 'compound_con',
       'compound_shifted_con', 'compound_shifted_tit', 'compound_tit',
       'volume', 'open_price', 'high', 'low']
x = data[cols]
x

data.columns

# scaling the feature dataset
scaler_x = preprocessing.MinMaxScaler (feature_range=(-1, 1))
x = npp.array(x).reshape((len(x) ,len(cols)))
x = scaler_x.fit_transform(x)

# scaling the target variable
scaler_y = preprocessing.MinMaxScaler (feature_range=(-1, 1))
y = npp.array (y).reshape ((len( y), 1))
y = scaler_y.fit_transform (y)

# displaying the scaled feature dataset and the target variable
x, y

# preparing training and test dataset
X_train = x[0 : train_end,]
X_test = x[train_end+1 : len(x),]    
y_train = y[0 : train_end] 
y_test = y[train_end+1 : len(y)]  

# printing the shape of the training and the test datasets
print('Number of rows and columns in the Training set X:', X_train.shape, 'and y:', y_train.shape)
print('Number of rows and columns in the Test set X:', X_test.shape, 'and y:', y_test.shape)

# reshaping the feature dataset for feeding into the model
X_train = X_train.reshape (X_train.shape + (1,)) 
X_test = X_test.reshape(X_test.shape + (1,))

# printing the re-shaped feature dataset
print('Shape of Training set X:', X_train.shape)
print('Shape of Test set X:', X_test.shape)

# setting the seed to achieve consistent and less random predictions at each execution
npp.random.seed(2016)

# setting the model architecture
model=Sequential()
model.add(LSTM(100,return_sequences=True,activation='tanh',input_shape=(len(cols),1)))
model.add(Dropout(0.1))
model.add(LSTM(100,return_sequences=True,activation='tanh'))
model.add(Dropout(0.1))
model.add(LSTM(100,activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(1))

# printing the model summary
model.summary()

# compiling the model
model.compile(loss='mse' , optimizer='adam')

# fitting the model using the training dataset
model.fit(X_train, y_train, validation_split=0.2, epochs=10, batch_size=8, verbose=1)

# performing predictions
predictions = model.predict(X_test) 

# unscaling the predictions
predictions = scaler_y.inverse_transform(npp.array(predictions).reshape((len(predictions), 1)))

# printing the predictions
print('Predictions:')
predictions[0:5]

# calculating the training mean-squared-error
train_loss = model.evaluate(X_train, y_train, batch_size = 1)

# calculating the test mean-squared-error
test_loss = model.evaluate(X_test, y_test, batch_size = 1)

# printing the training and the test mean-squared-errors
print('Train Loss =', round(train_loss,4))
print('Test Loss =', round(test_loss,4))

# calculating root mean squared error
root_mean_square_error = npp.sqrt(npp.mean(npp.power((y_test - predictions),2)))
print('Root Mean Square Error =', round(root_mean_square_error,4))

# calculating root mean squared error using sklearn.metrics package
rmse = metrics.mean_squared_error(y_test, predictions)
print('Root Mean Square Error (sklearn.metrics) =', round(npp.sqrt(rmse),4))

# unscaling the test feature dataset, x_test
X_test = scaler_x.inverse_transform(npp.array(X_test).reshape((len(X_test), len(cols))))

# unscaling the test y dataset, y_test
y_train = scaler_y.inverse_transform(npp.array(y_train).reshape((len(y_train), 1)))
y_test = scaler_y.inverse_transform(npp.array(y_test).reshape((len(y_test), 1)))

# plotting
plt.figure(figsize=(16,10))

# plt.plot([row[0] for row in y_train], label="Training Close Price")
plt.plot(predictions, label="Predicted Close Price")
plt.plot([row[0] for row in y_test], label="Testing Close Price")
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2)
plt.show()







