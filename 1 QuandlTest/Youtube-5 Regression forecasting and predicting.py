import pandas as pd
import quandl
import math , datetime
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
from matplotlib import style

import pickle

style.use('ggplot')

quandl.ApiConfig.api_key = "gAMrs6H3k6MaxsQMNFpL"
theData = quandl.get('WIKI/GOOGL')
theData = theData[['Adj. Open' , 'Adj. High' , 'Adj. Low' , 'Adj. Close' , 'Adj. Volume']]
theData['raiseStock'] = (theData['Adj. Close'] - theData['Adj. Open']) / theData['Adj. Open'] * 100

theData = theData[['Adj. Open' , 'Adj. Close' , 'raiseStock']]

#充填空值的欄位
theData.fillna(-99999 , inplace = True)
#ceil無條件進位
forecastOut = int(math.ceil(0.01*len(theData)))

#shift往左位移，EX:1->0 2->1
#往左位移，輸出預測
theData['forcastLabel'] = theData['Adj. Close'].shift(-forecastOut)

x = np.array(theData.drop(['forcastLabel'] , 1))
x = preprocessing.scale(x)
#前面len - forecastOut個單位
x = x[:-forecastOut]
#後面forecastOut個單位
x_lately = x[-forecastOut:]

theData.dropna(inplace = True)
y = np.array(theData['forcastLabel'])

xTrain , xTest , yTrain , yTest = cross_validation.train_test_split(x , y , test_size = 0.2)

#classfier
clf = LinearRegression()
clf.fit(xTrain , yTrain)
accuracy = clf.score(xTest , yTest)

forecastSet = clf.predict(x_lately)

theData['Forecast'] = np.nan

last_date = theData.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecastSet:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    #loc選擇數據用
    theData.loc[next_date] = [np.nan for _ in range(len(theData.columns) - 1)] + [i]
    
theData = theData[-100:]
theData['Adj. Close'].plot()
theData['Forecast'].plot()
plt.legend(loc = 4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()