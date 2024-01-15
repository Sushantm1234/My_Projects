#!/usr/bin/env python
# coding: utf-8

# # Netflix Stock Analysis Project

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[3]:


df = pd.read_csv("NFLX.csv")


# In[4]:


df


# In[5]:


df.head()


# In[6]:


df.tail()


# In[7]:


sns.set(rc = {'figure.figsize' : (10,5)})


# In[8]:


df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.head()


# In[9]:


sns.lineplot(x=df.index, y=df['Volume'], label='Volume')
plt.title('Volume of Stock vs Time')


# In[10]:


df.plot(y=['High','Close','Open'], title = 'Netflix Stock Price')


# In[14]:


fig, (ax1, ax2, ax3) = plt.subplots(3, figsize = (15,10))
df.groupby(df.index.day).mean().plot(y='Volume', ax=ax1, xlabel='Day')
df.groupby(df.index.month).mean().plot(y='Volume', ax=ax2, xlabel='Month')
df.groupby(df.index.year).mean().plot(y='Volume', ax=ax3, xlabel='Year')


# # Dates With Highest Stock Price

# In[15]:


df


# In[16]:


a = df.sort_values(by = 'High', ascending=False).head(5)
a['High']


# In[17]:


b = df.sort_values(by = 'Low', ascending=True).head(5)
b['Low']


# In[21]:


fig, axes = plt.subplots(nrows=1, ncols=2, sharex=True, figsize=(12,5))
fig.suptitle('High and Low Values Stock Per Period of Time', fontsize=18)
sns.lineplot(ax=axes[0], y=df['High'], x=df.index, color='green')
sns.lineplot(ax=axes[1], y=df['Low'], x=df.index, color='red')


# In[ ]:




