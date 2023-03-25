# -*- coding: utf-8 -*-
"""Copy of DSCI 521 Group Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nU57dQSw6Sa5HKE20N8iprtSSvwxcjYe

# ** A discussion of what you would like to your analysis to do, who/what it will support**

Our project is an attempt to predict the stock market using not only the stock data but headlines data as well.

We all know how Pepsi's stock value came crashing down when Ronaldo rejected it publicaly. We are trying to take in account the other variables that play a major role in stock market.
"""

! pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

import pandas as pd

stock_data = pd.read_csv('/content/NEWS_YAHOO_stock_prediction.csv')

from pandas_profiling import ProfileReport
#We only use the first 10000 data points
prof = ProfileReport(stock_data) 
prof.to_file(output_file='output.html')

profile = ProfileReport(stock_data)
profile.to_file(output_file="output_min.html")

"""# **Final EDA Report**"""

profile.to_notebook_iframe()