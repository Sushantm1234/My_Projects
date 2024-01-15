#!/usr/bin/env python
# coding: utf-8

# # i Phone Sales Analysis

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("apple_products.csv")


# In[3]:


data


# In[4]:


print(data.isnull().sum())


# In[5]:


print(data.describe())


# # iPhone Sales Analysis in India

# In[6]:


highest_rated = data.sort_values(by = ["Star Rating"], ascending = False)
hoghest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])


# # Let's have a look at the number of ratings of the highest rated iPhone on Flipkart

# In[13]:


iphones = highest_rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_rated["Number Of Ratings"]
figure = px.bar(highest_rated, x=labels, y=counts, title="Number of ratings of Highest rated iPhones")
figure.show()


# In[9]:


iphones


# In[15]:


iphones = highest_rated["Product Name"].value_counts()
labels = iphones.index
counts = highest_rated["Number Of Reviews"]
figure = px.bar(highest_rated, x=labels, y=counts, title="Number of reviews of Highest rated iPhones")
figure.show()


# In[16]:


figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size = "Discount Percentage", trendline="ols", title = "Relationship Between Sale Price and Number of Ratings")
figure.show()    


# In[18]:


figure = px.scatter(data_frame=data, x="Number Of Ratings", y="Discount Percentage", size = "Sale Price", trendline="ols", title = "Relationship Between Discount Percentage and Number of Ratings")
figure.show()


# In[ ]:




