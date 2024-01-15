#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('icc_wc_23_bowl.csv')
df.head()


# In[3]:


df.tail()


# In[4]:


df.isnull().sum()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df['team'].value_counts()


# # Data Analysis

# In[8]:


player_name = df.loc[df['runs'].idxmax(),'player']
team_name = df.loc[df['runs'].idxmax(),'team']
highest_runs = df.loc[df['runs'].idxmax(),'runs']
opponent = df.loc[df['runs'].idxmax(),'opponent']

print("'----> Highest Runs were given by the Bowler '",player_name,"'from the team of '",team_name,"'in one spell which are '",highest_runs,"against team",opponent)

player_name = df.loc[df['wickets'].idxmax(),'player']
team_name = df.loc[df['wickets'].idxmax(),'team']
highest_wickets = df.loc[df['wickets'].idxmax(),'wickets']
opponent = df.loc[df['wickets'].idxmax(),'opponent']

print("'----> Highest Wickets were taken by the Bowler '",player_name,"'from the team of '",team_name,"'in one spell which are '",highest_wickets,"against team",opponent)

player_name = df.loc[df['6s'].idxmax(),'player']
team_name = df.loc[df['6s'].idxmax(),'team']
highest_6s = df.loc[df['6s'].idxmax(),'6s']
opponent = df.loc[df['6s'].idxmax(),'opponent']

print("'----> Highest 6s were given by the Bowler '",player_name,"'from the team of '",team_name,"'in one spell which are '",highest_6s,"against team",opponent)

player_name = df.loc[df['4s'].idxmax(),'player']
team_name = df.loc[df['4s'].idxmax(),'team']
highest_4s = df.loc[df['4s'].idxmax(),'4s']
opponent = df.loc[df['4s'].idxmax(),'opponent']

print("'----> Highest 4s were given by the Bowler '",player_name,"'from the team of '",team_name,"'in one spell which are '",highest_4s,"against team",opponent)

player_name = df.loc[df['maidens'].idxmax(),'player']
team_name = df.loc[df['maidens'].idxmax(),'team']
highest_maidens = df.loc[df['maidens'].idxmax(),'maidens']
opponent = df.loc[df['maidens'].idxmax(),'opponent']

print("'----> Highest Runs were given by the Bowler '",player_name,"'from the team of '",team_name,"'in one spell which are '",highest_maidens,"against team",opponent)







# In[9]:


# group the players by the overs, runs, wickets.......
df_player_overs = df.groupby('player').agg({'overs':'sum', 'maidens':'sum', 'runs':'sum', 'wickets':'sum', 'run_rate':'mean', '4s':'sum', '6s':'sum', 'wd':'sum'}).reset_index()


# In[10]:


# sort the dataset by overs
sorted_df_player_overs = df_player_overs.sort_values(by='overs', ascending=False).reset_index()


# In[11]:


sorted_df_player_overs


# # Plot the Bar graph between Overs and Players

# In[12]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

#plotting
plt.figure(figsize=(20,6))
plt.bar(df_player_overs_top_30['player'],df_player_overs_top_30['overs'])
plt.xlabel('Player')
plt.ylabel('overs')
plt.title('Overs by the Top 30 PLayers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# show the plot
plt.show()


# Runs given by the Top 30 Bowlers

# In[13]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

#plotting
plt.figure(figsize=(15,6))
plt.bar(df_player_overs_top_30['player'],df_player_overs_top_30['runs'], color='violet')
plt.xlabel('Player')
plt.ylabel('runs')
plt.title('Runs given by the Top 30 PLayers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# show the plot
plt.show()


# Run Rate given by the Top 30 Bowlers

# In[14]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

#plotting
plt.figure(figsize=(15,6))
plt.bar(df_player_overs_top_30['player'],df_player_overs_top_30['run_rate'], color='orange')
plt.xlabel('Player')
plt.ylabel('run_rate')
plt.title('Run_rate given by the Top 30 PLayers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# show the plot
plt.show()


# Wide Balls from the Top 30 Bowlers

# In[15]:


df_player_overs_top_30 = sorted_df_player_overs.head(30)

#plotting
plt.figure(figsize=(15,6))
plt.bar(df_player_overs_top_30['player'],df_player_overs_top_30['wd'], color='pink')
plt.xlabel('Player')
plt.ylabel('Wide balls')
plt.title('Wide balls given from the Top 30 Bowlers')
plt.xticks(rotation=45, ha='right')  # Rotate player names for better visibility
plt.tight_layout()

# show the plot
plt.show()


# Maiden overs and Overs for the Top 30 players

# In[16]:


fig, ax1 = plt.subplots(figsize=(12,6))

# Plot bars for 'overs' on the primary y-axis(ax1) 
index = np.arange(len(df_player_overs_top_30))
bars = ax1.bar(index, df_player_overs_top_30['overs'], label='Overs', color = 'skyblue')

# Plot line for 'Wickets' on the same y-axis(ax1) 
line = ax1.plot(index, df_player_overs_top_30['maidens'], label='maidens', marker='o', color = 'orange')

# Set Labels and Titles
ax1.set_xlabel('Player')
ax1.set_ylabel('Overs', color='skyblue')    # Make sure y-axis labels are in blue

plt.title('Maidens overs and Overs for the top 30 players')

# combine legends
bars_legend = [bar for bar in bars]
line_legend = [line[0]]
plt.legend(bars_legend + line_legend, ['Overs','Maiden'], loc ='upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_overs_top_30['player'], rotation=45, ha='right')

# Show the plot 
plt.tight_layout()
plt.show()


# # Bowlers are Sorted on the wickets taken by them 

# In[17]:


sorted_df_player_wickets = df_player_overs.sort_values(by='wickets', ascending=False).reset_index()
sorted_df_player_wickets


# Wickets taken by the top 30 bowlers

# In[18]:


df_player_wickets_top_30 = sorted_df_player_wickets.head(30)

# plotting
plt.figure(figsize=(15,6))
plt.bar(df_player_wickets_top_30['player'], df_player_wickets_top_30['wickets'], color='violet')
plt.xlabel('Player')
plt.ylabel('wickets')
plt.title('wickets taken by the top 30 bowlers')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show
plt.show()


# Wickets and overs for the top 30 Players

# In[19]:


# create a figure and axis
fig, ax1 = plt.subplots(figsize=(12,6))

# plot bars for 'overs' on the primary y-axis (ax1)
index = np.arange(len(df_player_wickets_top_30))
bars = ax1.bar(index, df_player_wickets_top_30['overs'], label='Overs', color='skyblue')

# plot line for 'wickets' on the same y-axis (ax1)
line = ax1.plot(index, df_player_wickets_top_30['wickets'], color='orange',marker='o', label='Wickets')

# set labels and titles
ax1.set_xlabel('Player')
ax1.set_ylabel('Overs', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')    # Make sure y-axis labels are in blue

plt.title('Wickets and overs for the top 30 players')

# combine legends
bars_legend = [bars for bar in bars]
line_legend = [line[0]]
plt.legend(bars_legend + line_legend, ['Overs','Wickets'], loc='upper left')

# Set x-axis ticks and labels
plt.xticks(index, df_player_wickets_top_30['player'], rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()



# 4s given by the top 30 bowlers

# In[20]:


df_player_wickets_top_30 = sorted_df_player_wickets.head(30)

# plotting
plt.figure(figsize=(15,6))
plt.bar(df_player_wickets_top_30['player'], df_player_wickets_top_30['4s'], color='cyan')
plt.xlabel('Player')
plt.ylabel('4s')
plt.title('4s given by the top 30 bowlers')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show
plt.show()


# 6s given by the top 30 bowlers

# In[21]:


# plotting
plt.figure(figsize=(15,6))
plt.plot(df_player_wickets_top_30['player'], df_player_wickets_top_30['6s'], marker='o',linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Player')
plt.ylabel('6s')
plt.title('6s given by the top 30 bowlers')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show the plot
plt.show()
plt.show()


# # Group by Team

# In[31]:


df_team_overs = df.groupby('team').agg({'overs':'sum', 'maidens':'sum', 'runs':'sum', 'wickets':'sum', 'run_rate':'mean', '4s':'sum', '6s':'sum', 'wd':'sum'}).reset_index()
df_team_overs


# Overs by Each Team

# In[23]:


# plotting
plt.figure(figsize=(15,6))
plt.bar(df_team_overs['team'], df_team_overs['overs'], color='magenta')
plt.xlabel('Team')
plt.ylabel('overs')
plt.title('Overs by each Team')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show
plt.show()


# Maiden overs each Team 

# In[32]:


# plotting
plt.figure(figsize=(10,6))
plt.bar(df_team_overs['team'], df_team_overs['maidens'])
plt.xlabel('Team')
plt.ylabel('maiden overs')
plt.title('maiden overs by each Team')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show
plt.show()


# Run_rate by the team bowlers

# In[33]:


# plotting
plt.figure(figsize=(12,6))
plt.plot(df_team_overs['team'], df_team_overs['run_rate'], marker='o', linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('run_rate')
plt.title('Run_rate given by the Team Bowlers')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show the plot
plt.show()
plt.show()
plt.show()


# Wickets taken by Each Team

# In[36]:


plt.figure(figsize=(8,8))
plt.pie(df_team_overs['wickets'], labels=df_team_overs['team'])
plt.title('Wickets taken by Each Team')
#plt.axis('equal')    #Equal aspect ratio ensures that the pie is drawn as a circle

plt.show()


# In[35]:


# plotting
plt.figure(figsize=(15,6))
plt.plot(df_team_overs['team'], df_team_overs['runs'], marker='o', linestyle='--')
plt.grid()
plt.gray()
plt.xlabel('Teams')
plt.ylabel('runs')
plt.title('Runs given by the Team Bowlers')
plt.xticks(rotation=45, ha='right')    # Rotate player names for better visbility
plt.tight_layout()

# show the plot
plt.show()


# Wides by Each Team

# In[37]:


plt.figure(figsize=(8,8))
plt.pie(df_team_overs['wd'], labels=df_team_overs['team'])
plt.title('Wides by Each Team')
#plt.axis('equal')    #Equal aspect ratio ensures that the pie is drawn as a circle

plt.show()


# In[ ]:




