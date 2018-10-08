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

#在-2~4區間，取100個點做畫圖基礎
x0 = np.linspace(-2,4,100)

#利用Numpy的函數訓練函數
#deg代表函式的最高次方項
#返回模型所訓練的預測的y

def getModel(deg):
    return lambda input_x = x0 : np.polyval( np.polyfit(x,y,deg) , input_x )


def getCost(deg, inputX, inputY):
    return 0.5 * ( (getModel(deg)(inputX) - inputY) ** 2 ).sum()

#定義測試函式集，1,4,10項次
testSet = (1,4,10)

#輸出相應的損失
for lost in testSet:
    print("N = " + str(lost)
    + " " + str( getCost(lost , x , y) ) )
    
plt.scatter(x, y, c="g", s=20)

for n in testSet:
    plt.plot(x0, getModel(n)(), label="degree = {}".format(n))
    
#限制x,y軸間距
plt.xlim(-2,4)
plt.ylim(1e5,8e5)

#為了顯示label
plt.legend()

plt.title("plot")
plt.xlabel("house area index")
plt.ylabel("house price")
plt.show()