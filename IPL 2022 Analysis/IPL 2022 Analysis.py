#!/usr/bin/env python
# coding: utf-8

# # IPL Data Analysis Project

# In[1]:


import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("ipl2022.csv")


# In[3]:


data


# # Number of Matches won by Each Team in IPL 2022

# In[4]:


figure = px.bar(data, x=data['match_winner'], title="Number of Matches Won in IPL 2022")
figure.show()


# In[5]:


data["won_by"] = data["won_by"].map({"Wickets":"Chasing", "Runs":"Defending"})
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['red','lightgreen']
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Number of matches won by defending or chasing")
fig.update_traces(hoverinfo = 'label+percent', textinfo = 'value', textfont_size = 30, marker = dict(colors=colors, line=dict(color = 'black', width=3)))


# In[6]:


figure = px.bar(data, x=data["best_bowling"], title="Best Bowler in IPL 2022")
figure.show()


# In[7]:


figure = px.bar(data, x=['player_of_the_match'], title = "Most Player of the Match Awards")
figure.show()


# # Top Scorer in IPL 2022

# In[10]:


figure = px.bar(data, x=data["top_scorer"], y=data['highscore'], color=data['highscore'], title="Top Scorers in IPL 2022")
figure.show()


# In[ ]:




