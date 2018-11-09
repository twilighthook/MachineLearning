import pandas as pd
import quandl

quandl.ApiConfig.api_key = "gAMrs6H3k6MaxsQMNFpL"
theData = quandl.get('WIKI/GOOGL')
theData = theData[['Adj. Open' , 'Adj. High' , 'Adj. Low' , 'Adj. Close' , 'Adj. Volume']]
theData['raiseStock'] = (theData['Adj. High'] - theData['Adj. Open']) / theData['Adj. Open'] * 100

theData = theData[['Adj. Open' , 'Adj. High' , 'raiseStock']]

print(theData.tail(20))