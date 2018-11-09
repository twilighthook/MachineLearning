# -*- coding: utf-8 -*-

import numpy as np

class NaiveBayes:
    """
        初始結構
        self._x, self._y，存訓練的變數
        self._data 存條件機率的數組
        self._func 存後驗機率的決策函數
        self._nPossibilities 存個維度的特徵取值的數組: [S1,S2...Sn
        self._labelX 記錄存輸入的數組
        self._labelZip 紀錄數組訊息
        self._catCount 記錄第N類數據的個數 category
        self._conCount 記錄其條件機率 condition
        self._labelDic 核心字典，紀錄數值轉化過程的關係
        selt._featDic 記錄各維度特徵轉化關係
    """
    
    def init(self):
        self._x = self._y = None
        self._data = self._func = None
        self._nPossibilities = None
        self._labelX = self._labelZip = None
        self._catCount = self._conCount = None
        self._labelDic = self._featDic = None
        
    def getItem(self , item):
        #檢查item是否為str
        if isinstance(item , str): 
            #??
            return getattr(self , "_" + item)
        
    def feedData(self , x , sampleWeight = None):
        pass
    
    #sampleWeight = 樣本權重
    def feedSampleWeight(self, sampleWeight = None):
        pass
    
    def getPriorProbability(self, lb=1):
        return [(cNum + lb) / (len(self._y) + lb * len(self._catCounter) ) 
                for cNum in self._catCount]
    
        
    