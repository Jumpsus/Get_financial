# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:49:39 2021

@author: Jumpsus
"""
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as ur
import json

Stock = "AOT.BK" 
# Stock Symbol in Reuter Website.
#   If you not sure Symbols of stock, Do mannual search in https://www.reuters.com


def get_income_statement(Stock):
    url = 'https://www.reuters.com/companies/'+ Stock +'/financials' #url for request data
    read = ur.urlopen(url).read() #request data from web inthis process you need to connect internet
    soup = BeautifulSoup(read,'lxml')
    B = json.loads(soup.find_all('script')[4].string) #convert json script to dictionary, [4] is position of script that content financial data
    df = pd.DataFrame(columns=B['props']['initialState']['markets']['financials']['financial_tables']['income_annual_tables'][0]['headers']) #create dataframe
    for i in B['props']['initialState']['markets']['financials']['financial_tables']['income_annual_tables'][0]['rows']:
        name = i['name']
        for j in i['data']:
            try:
                df.loc[name,j['date']] = j['value']
            except:
                print(name," have missing data")
    return df    

