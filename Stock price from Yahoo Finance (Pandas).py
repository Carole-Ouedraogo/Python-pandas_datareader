#!/usr/bin/env python
# coding: utf-8

# In[79]:


print('Tesla Stock Price Trends In 2019')


# In[80]:


from pandas_datareader import data


# In[81]:


tesla = data.DataReader('tsla', start='2019-01-01', end='2019-12-31', data_source='yahoo')
tesla.head()


# In[82]:


print(tesla[['Close']])


# In[71]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


# In[72]:


tesla.plot()

