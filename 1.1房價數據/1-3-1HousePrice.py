# -*- coding: utf-8 -*-

# 支援高階的矩陣運算擴充函式庫
import numpy as np
# 圖形用戶界面工具包
import matplotlib.pyplot as plt

x , y = [] , []

#獲取數據集，並以浮點方式匯入陣列
for sample in open("HousePrice.txt" , "r"):
    _x, _y = sample.split(",")
    x.append(float(_x))
    y.append(float(_y))
    
#讀取數據候用Numpy存成Numpy數據組
x,y = np.array(x) , np.array(y)

#標準化X數據庫
x = (x - x.mean()) / x.std()

#以pyplot輸出圖表
plt.figure()
plt.scatter(x,y,c='g',s=6)

#color for red
plt.title("plot")
plt.xlabel("house area index")
plt.ylabel("house price")
plt.show()