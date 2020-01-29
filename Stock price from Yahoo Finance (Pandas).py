#!/usr/bin/env python
# coding: utf-8

print('Tesla Stock Price Trends In 2019')

from pandas_datareader import data

#2019 stock trends of Tesla Inc as a DataFrame.

tesla = data.DataReader('tsla', start='2019-01-01', end='2019-12-31', data_source='yahoo')
tesla.head()

# How to display a single column
print(tesla[['Close']])

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

# Visualizing with the plot() method
tesla.plot()
pandas-datareader

