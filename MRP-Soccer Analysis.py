#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


teamdf = pd.read_csv("D:\My Datasets!!!\SLUSOCCER.csv")


# In[3]:


teamdf.head()


# In[4]:


teamdf = teamdf.rename(columns={"Individual Overall Offensive Statistics": "Jersey", "Unnamed: 1": "Player",
                         "Unnamed: 2": "Games_played", "Unnamed: 3": "Mins_Started", "Unnamed: 4": "Mins",
                         "Unnamed: 5": "Goals", "Unnamed: 6": "Assists", "Unnamed: 7": "Points",
                         "Unnamed: 8": "Shots", "Unnamed: 9": "Shots_Percentage", "Unnamed: 10": "Shots_On_Goals",
                         "Unnamed: 11": "Shots_on_Goals_Percentage", "Unnamed: 12": "YellowCard", "Unnamed: 13": "RedCard",
                         "Unnamed: 14": "Games_Winning_Goals", "Unnamed: 15": "Penalty_Goals", "Unnamed: 16": "Penalty_Attempts"})


# In[5]:


teamdf.head(2)


# In[6]:


teamdf = teamdf.drop(labels=0, axis=0)


# In[7]:


teamdf.head()


# In[8]:


len(teamdf)


# In[9]:


teamdf.info()


# In[10]:


teamdf.describe()


# In[11]:


teamdf['Position'] = ['MF', 'FW', 'DF', 'FW', 'CDM', 'MF', 'MF', 'DF', 'CDM', 'CAM', 'CAM', 'CDM', 'CDM', 'CAM', 'MF', 'MF', 'MF', 'FW', 'DF', 'FW', 'FW', 'DF', 'GK', 'GK', 'CDM', 'CDM', 'CDM', 'GK', 'CDM','-']


# In[12]:


teamdf.head(2)


# In[13]:


cols = list(teamdf.columns.values)


# In[14]:


teamdf = teamdf[cols[0:2] + [cols[-1]] + cols[2:18]]


# In[15]:


teamdf.head()


# In[16]:


teamdf.to_csv('teamdf.csv', index=False)


# In[17]:



# players who played the games had also started the games.

players = teamdf.loc[teamdf['Games_played'] == teamdf['Mins_Started'], 'Player']
players


# In[117]:



#Penalties_missed = Penalty_Attempts - Penalty_Goals


# In[118]:


#activity = teamdf[teamdf[Goals] + teamdf[Assists]]


# In[119]:


#teamdf.head(3)


# In[120]:


#Penalties_missed = Penalty_Attempts - Penalty_Goals


# In[121]:


#teamdf['Penalties_Missed'] = teamdf[teamdf['Penalty_Attempts'] - teamdf['Penalty_Goals']]


# In[18]:


teamdf.dtypes


# In[19]:


teamdf['Penalty_Goals'] = teamdf['Penalty_Goals'].astype(int)


# In[20]:


teamdf['Penalty_Attempts'] = teamdf['Penalty_Attempts'].astype(int)


# In[21]:


teamdf.dtypes


# In[22]:


#Penalties_missed = Penalty_Attempts - Penalty_Goals


# In[23]:


#teamdf['Penalties_Missed'] = teamdf[teamdf['Penalty_Attempts'] - teamdf['Penalty_Goals']]


# In[24]:


#teamdf['Penalties_Missed'] = teamdf['Penalty_Attempts'] - teamdf['Penalty_Goals']


# In[25]:


teamdf


# In[26]:


Penalty_Goals = teamdf['Penalty_Goals'].sum()
Penalty_Goals


# In[27]:


Penalty_Attempts = teamdf['Penalty_Attempts'].sum()
Penalty_Attempts


# In[28]:


plt.figure(figsize=(12,6))
Penalties_Missed = Penalty_Attempts - Penalty_Goals
data = [Penalties_Missed, Penalty_Goals]
labels = ['Penaltymissed','PenaltyGoals' ]
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct='%.0f%%')
plt.show()


# In[ ]:





# In[29]:


teamdf.tail()


# In[30]:


daytondf = pd.read_excel("D:\My Datasets!!!\Dayton team.xlsx")


# In[31]:


daytondf.head()


# In[32]:


daytondf = daytondf.rename(columns={"Unnamed: 0": "Jersey", "Unnamed: 1": "Player",
                         "Unnamed: 2": "Games_played", "Unnamed: 3": "Mins_Started", "Unnamed: 4": "Mins",
                         "Unnamed: 5": "Goals", "Unnamed: 6": "Assists", "Unnamed: 7": "Points",
                         "Unnamed: 8": "Shots", "Unnamed: 9": "Shots_Percentage", "Unnamed: 10": "Shots_On_Goals",
                         "Unnamed: 11": "Shots_on_Goals_Percentage", "Unnamed: 12": "YellowCard", "Unnamed: 13": "RedCard",
                         "Unnamed: 14": "Games_Winning_Goals", "Unnamed: 15": "Penalty_Goals", "Unnamed: 16": "Penalty_Attempts"})


# In[33]:


daytondf.head(2)


# In[34]:


daytondf


# In[35]:


daytondf = daytondf.drop([0, 1])


# In[36]:


daytondf.head()


# In[37]:


daytondf = daytondf.drop([2])


# In[38]:


daytondf.head()


# In[40]:


#daytondf['Position'] = ['FW', 'FW', 'CAM', 'MF', 'MF', 'MF', 'FW', 'DF', 'DF', 'FW', 'DF', 'DF', 'CAM', 'MF', 'GK', 'DF', 'DF', 'FW', 'DF', 'DF', 'CAM', 'DF', 'MF','-','-','-']


# In[42]:


daytondf.head(3)


# In[43]:


cols = list(teamdf.columns.values)


# In[45]:


#daytondf = daytondf[cols[0:2] + [cols[-1]] + cols[2:18]]


# In[46]:


daytondf.head()


# In[50]:



# Daytonplayers who played the games had also started the games.

daytonplayers = daytondf.loc[daytondf['Games_played'] == daytondf['Mins_Started'], 'Player']

daytonplayers


# In[54]:



daytondf['Games_played'] = daytondf['Games_played'].astype('int')
daytondf['Mins_Started'] = daytondf['Mins_Started'].astype('int')
daytondf['Player'] = daytondf['Player'].astype('int')


# In[61]:




#daytonplayers = daytondf.loc[teamdf['Games_played'] == daytondf['Mins_Started'], 'Player']
#daytonplayers


# In[62]:


#daytondf = daytondf.drop([2])


# In[59]:


daytondf.head(3)


# In[60]:




daytonplayers = daytondf.loc[daytondf['Games_played'] == daytondf['Mins_Started'], 'Player']
daytonplayers


# In[63]:


Penalty_Goals = daytondf['Penalty_Goals'].sum()
Penalty_Goals


# In[64]:


Penalty_Attempts = daytondf['Penalty_Attempts'].sum()
Penalty_Attempts


# In[ ]:


plt.figure(figsize=(12,6))
Penalties_Missed = Penalty_Attempts - Penalty_Goals
data = [Penalties_Missed, Penalty_Goals]
labels = ['Penaltymissed','PenaltyGoals' ]
color = sns.color_palette('Set2')
plt.pie(data, labels = labels, colors = color, autopct='%.0f%%')
plt.show()


# In[66]:


import matplotlib.pyplot as plt
import seaborn as sns

# define the data and labels
Penalty_Attempts = 20
Penalty_Goals = 15
Penalties_Missed = Penalty_Attempts - Penalty_Goals
data = [Penalties_Missed, Penalty_Goals]
labels = ['Penalty missed', 'Penalty goals']
colors = sns.color_palette('Set2')

# create the pie chart
plt.figure(figsize=(12, 6))
plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
plt.show()


# In[ ]:


daytondf


# In[ ]:


daytondf.loc[1, 'Penalty_Attempts'] = 1


# In[ ]:


daytondf.head(3)


# In[ ]:


daytondf.to_csv('daytondf.csv', index=False)


# In[ ]:


daytondf = pd.read_csv('D:\My Datasets!!!\daytondf.csv')


# In[ ]:


daytondf.head(3)


# In[146]:



# define the data and labels
Penalty_Attempts = 2
Penalty_Goals = 2
Penalties_Missed = Penalty_Attempts - Penalty_Goals
data = [Penalties_Missed, Penalty_Goals]
labels = ['Penalty missed', 'Penalty goals']
colors = sns.color_palette('dark')

# create the pie chart
plt.figure(figsize=(12, 6))
plt.pie(data, labels=labels, colors=colors, autopct='%.0f%%')
plt.show()


# In[147]:


get_ipython().system('pip install mplsoccer')


# In[148]:


from mplsoccer.pitch import Pitch


# In[149]:


johndf = pd.read_csv("C:/Users/N.P.Sreekar/Downloads/KJPasses.csv")


# In[150]:


johndf.head()


# In[151]:


johndf['x'] = johndf['x']*1.2
johndf['y'] = johndf['y']*0.8
johndf['endX'] = johndf['endY']*1.2
johndf['endY'] = johndf['endY']*0.8


# In[152]:


johndf.head(3)


# In[153]:


pitch = Pitch(line_zorder=2)
fig, ax = pitch.draw(figsize=(16, 9), tight_layout=False)

# add an image
ax_image = add_image("C:\Users\N.P.Sreekar\Downloads\kj photo.jpeg", fig, left=0.55, bottom=0.2, width=0.2,
                     alpha=0.9, interpolation='hanning')


# In[ ]:


from matplotlib.image import imread


# In[ ]:


def add_image(image_path, fig, left, bottom, width, alpha, interpolation):
    image = imread(image_path)
    ax_image = fig.add_axes([left, bottom, width, width * image.shape[0] / image.shape[1]])
    ax_image.imshow(image, alpha=alpha, interpolation=interpolation)
    ax_image.axis('off')
    return ax_image


# In[159]:


pitch = Pitch(line_zorder=2)
fig, ax = pitch.draw(figsize=(16, 9), tight_layout=False)


ax_image = add_image(r"C:/Users/N.P.Sreekar/Downloads/kj photo.jpeg", fig, left=0.4, bottom=0.5, width=0.3,
                     alpha=0.9, interpolation='hanning')


# In[154]:


fig,ax = plt.subplots(figsize=(12,9))
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')
#pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc', figsize=(15,10),
          #   constarined_layout=True, tight_layout=False)
#pitch.draw(ax=ax)
#plt.gca().invert_yaxis()


# In[155]:


pitch = Pitch(line_zorder=2)
fig, ax = pitch.draw(figsize=(16, 9), tight_layout=False)
ax.patch.set_facecolor('#22312b')
pitch.draw(ax=ax)


# In[158]:


pitch = Pitch(pitch_type='statsbomb', pitch_color='#22312b', line_color='#c7d5cc')
fig, ax = pitch.draw(figsize=(7.5, 9), constrained_layout=True, tight_layout=False)
fig.set_facecolor("#22312b")

for x in range(len(johndf['x'])):
    if johndf['outcome'][x] == 'Successful':
        plt.plot((johndf['x'][x], johndf['endX'][x]), (johndf['y'][x], johndf['endY'][x]), color='green')
    if johndf['outcome'][x] == 'Unsuccessful':
        plt.plot((johndf['x'][x], johndf['endX'][x]), (johndf['y'][x], johndf['endY'][x]), color='red')


# In[ ]:




