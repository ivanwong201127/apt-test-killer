import pandas as pd
import numpy as np
from datetime import datetime

import yfinance as yf
from matplotlib import pyplot as plt
from matplotlib import style
import scipy.stats as stats

import requests
import bs4 as bs
from urllib.parse import urlencode
import json
import os

class asset:
    def __init__(self,code):
        self.code = code

    def set_time(self, period, start, end):
        self.period = period
        self.start = start
        self.end = end

    def get_data(self):
        if self.period != None or self.start != None or self.end != None:
            stock = yf.Ticker(self.code).history(period=self.period,start=self.start,end=self.end)
            self.price = stock[["Open","Close","High","Low","Volume"]]
        else:
            print("Please set the date first")

baba = asset("9988.HK")
baba.set_time("1y",None,None)
baba.get_data()
baba_price = baba.price

# Ploting Bolliner Band
baba_mean = baba_price["Close"].rolling(10).mean()[10:]
baba_std = baba_price["Close"].rolling(10).std()[10:]

# Use bollinger band overbuy over sold
style.use("ggplot")
plt.plot(baba_price.index,baba_price["Close"])
plt.plot(baba_price.index[10:],baba_mean,color="b")
plt.plot(baba_price.index[10:],baba_mean+2*baba_std,color="k",linestyle="--")
plt.plot(baba_price.index[10:],baba_mean-2*baba_std,color="k",linestyle="--")
plt.show()