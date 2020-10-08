import pandas as pd
import numpy as np
from datetime import datetime

import yfinance as yf
from matplotlib import pyplot as plt

import requests
import bs4 as bs
from urllib.parse import urlencode
import json
import os

def get_hsi_stocks(name="hsi"):
    hsi_stock_list = pd.DataFrame(columns=["code","company"])

    data = requests.get("https://hk.finance.yahoo.com/quote/%5EHSI/components?p=%5EHSI")
    resp = data.text.encode('utf-8')
    soup = bs.BeautifulSoup(resp,'lxml')
    stock_listings = soup.find("tbody").find_all("tr")

    for stock in stock_listings:
        info = stock.find_all("td")
        code = info[0].find("a")["title"]
        company = info[1].text
        hsi_stock_list.loc[len(hsi_stock_list)] = [code,company]


    if not os.path.exists("./stocks/{}".format(name)):
        os.mkdir("./stocks/{}".format(name))

    hsi_stock_list.to_csv("./stocks/{}/{}_stock_list.csv".format(name,name),encoding="utf-8")
    print("{} Stocks Update Successful".format(name))

def get_stocks(url, name):
    hsi_stock_list = pd.DataFrame(columns=["code","company"])

    data = requests.get(url)
    resp = data.text.encode('utf-8')
    soup = bs.BeautifulSoup(resp,'lxml')
    stock_listings = soup.find("tbody").find_all("tr")

    for stock in stock_listings:
        info = stock.find("td")
        company = info.find("a")["title"]
        code = info.find("a").text
        hsi_stock_list.loc[len(hsi_stock_list)] = [code,company]

    if not os.path.exists("./stocks/{}".format(name)):
        os.mkdir("./stocks/{}".format(name))

    hsi_stock_list.to_csv("./stocks/{}/{}_stock_list.csv".format(name,name),encoding="utf-8")
    print("{} Stocks Update Successful".format(name))

yahoo_industries = {"energy":"https://hk.finance.yahoo.com/industries/energy",
                    "financial":"https://hk.finance.yahoo.com/industries/financial",
                    "healthcare":"https://hk.finance.yahoo.com/industries/healthcare",
                    "business":"https://hk.finance.yahoo.com/industries/business_services",
                    "telecom":"https://hk.finance.yahoo.com/industries/telecom_utilities",
                    "electronics":"https://hk.finance.yahoo.com/industries/hardware_electronics",
                    "software":"https://hk.finance.yahoo.com/industries/software_services",
                    "manufacturing":"https://hk.finance.yahoo.com/industries/manufacturing_materials",
                    "consumer":"https://hk.finance.yahoo.com/industries/consumer_products_media",
                    "industrial":"https://hk.finance.yahoo.com/industries/industrials",
                    "conglomerate":"https://hk.finance.yahoo.com/industries/diversified_business",
                    "retail":"https://hk.finance.yahoo.com/industries/retailing_hospitality"
                    }

get_hsi_stocks()
for idx,val in yahoo_industries.items():
    get_stocks(val,idx)