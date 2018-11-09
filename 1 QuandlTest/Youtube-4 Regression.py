import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing , cross_validation , svm
from sklearn.linear_model import LinearRegression

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
#將有none值的row刪除
theData.dropna(inplace = True)

#x為三個預測參數，open close raise，y為35天后的股票

#axis default給予
x = np.array(theData.drop(['forcastLabel'] , axis=1))
y = np.array(theData['forcastLabel'])

#X1 = (X-X_mean)/X_std
#use function preprocessing.scale to standardize X
#X_scale = preprocessing.scale(X)
#two answer is equal

x = preprocessing.scale(x)
y = np.array(theData['forcastLabel'])    

#四個參數為固定用法，test_sizeh從0~1代表dataset的比例
xTrain , xTest , yTrain , yTest = cross_validation.train_test_split(x , y , test_size = 0.2)

#classfier
clf = LinearRegression()
#開多執行續，if n_jobs = -1 use all processor
#clf = LinearRegression(n_jobs = 10)
#clf = svm.SVR()
#clf = svm.SVR(kernel = 'poly')
clf.fit(xTrain , yTrain)
accuracy = clf.score(xTest , yTest)

print(accuracy)
