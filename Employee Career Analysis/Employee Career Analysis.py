#!/usr/bin/env python
# coding: utf-8

# # Employee Career Survey Analysis

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("Your Career Aspirations of GenZ.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.columns


# In[6]:


unique_countries = data['Your Current Country.'].unique()


# In[7]:


unique_countries


# In[8]:


country = data['Your Current Country.'].value_counts()
label = country.index
counts = country.values
colors = ['red','lightgreen']
fig = go.Figure(data = [go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Current Country")
fig.update_traces(hoverinfo='label+value', textinfo = 'percent', textfont_size=30, marker=dict(colors=colors, line=dict(color='black',width=3)))
fig.show()


# In[9]:


country


# Objective 2 :  Factors influencing Career Aspirations

# In[10]:


data.head()


# In[18]:


question1 = "Which of the below factors influence the most about your career aspirations ?"
question1 = data[question1].value_counts()
label = question1.index
counts = question1.values
colors = ['gold','lightgreen']
fig = go.Figure(data = [go.Pie(labels=label, values = counts)])
fig.update_layout(title_text='Factors influecing Career Aspirations')
fig.update_traces(hoverinfo='label+value', textinfo = 'percent', textfont_size=30, marker=dict(colors=colors, line=dict(color='black',width=3)))
fig.show()


# Objective 3 :

# In[12]:


question2 ="Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2 = data[question2].value_counts()    


# In[13]:


question2


# In[14]:


question2.index


# In[15]:


question2.count


# In[16]:


question2 ="Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2 = data[question2].value_counts() 
label = question2.index
counts = question2.values
colors = ['orange','black']
fig = go.Figure(data = [go.Pie(labels=label, values = counts)])
fig.update_layout(title_text='Factors influecing Career Aspirations')
fig.update_traces(hoverinfo='label+value', textinfo = 'percent', textfont_size=30, marker=dict(colors=colors, line=dict(color='black',width=3)))
fig.show()


# Objective 4 :-

# In[19]:


data.head()


# In[21]:


question3 = "How likely is that you will work for one employer for 3 years or more ?"
question3 = data[question3].value_counts()


# In[22]:


question3


# In[23]:


question3.index


# In[25]:


question3.count


# In[26]:


question3 = "How likely is that you will work for one employer for 3 years or more ?"
question3 = data[question3].value_counts()
label = question3.index
counts = question3.values
colors = ['aqua','red']
fig = go.Figure(data = [go.Pie(labels=label, values = counts)])
fig.update_layout(title_text='How likey is that you will work in one company')
fig.update_traces(hoverinfo='label+value', textinfo = 'percent', textfont_size=30, marker=dict(colors=colors, line=dict(color='black',width=3)))
fig.show()


# Objective 5 :-

# In[27]:


data.head()


# In[28]:


question5 = "What is the most preferred working environment for you."
question5 = data[question5].value_counts()


# In[29]:


question5 


# In[30]:


question5.index


# In[31]:


question5.count


# In[34]:


question5 = "What is the most preferred working environment for you."
question5 = data[question5].value_counts()
label = question5.index
counts = question5.values
colors = ['green','magenta']
fig= go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Most preferred working environment for Employee')
fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=30, marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()


# In[ ]:




