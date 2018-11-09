import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = "gAMrs6H3k6MaxsQMNFpL"
theData = quandl.get('WIKI/GOOGL')
theData = theData[['Adj. Open' , 'Adj. High' , 'Adj. Low' , 'Adj. Close' , 'Adj. Volume']]
theData['raiseStock'] = (theData['Adj. Close'] - theData['Adj. Open']) / theData['Adj. Open'] * 100

theData = theData[['Adj. Open' , 'Adj. Close' , 'raiseStock']]

forecastCol = 'Adj. Close'

#充填空值的欄位
theData.fillna(-99999 , inplace = True)

#無條件進位
forecastOut = int(math.ceil(0.01*len(theData)))

#shift往左位移，EX:1->0 2->1
#往左位移，輸出預測
theData['forcastLabel'] = theData[forecastCol].shift(-forecastOut)

theData.dropna(inplace = True)

print(theData.tail())