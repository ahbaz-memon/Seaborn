#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# # Catagorical plot
# 
# ### 1. categorical scatterplots
# ##### a. strip-plot 
# ##### b. swarmplot
# 
# ### 2. categorical distribution plots
# ##### a. box-plot 
# ##### b. violin-plot
# 
# ### 3. categorical estimate plots
# ##### a. Point-plot 
# ##### b. bar-plot
# ##### c. count-plot
# 
# ### 4. categorical categorical plots
# ##### a. Heat-maps
# ##### b. cluster-maps
# 

# In[2]:


plt.style.use('fivethirtyeight')#styling for beauty


# In[3]:


data=sns.load_dataset('tips')


# In[4]:


data.head()


# ### 1. categorical scatterplots

# ##### a. strip-plot 

# In[5]:


sns.catplot(x='day',y='tip',data=data,kind='strip')
#can also use -> sns.stripplot(x='day',y='tip',data=data)


# In[6]:


sns.catplot(x='day',
            y='tip',
            data=data,
            kind='strip',
            jitter=2 #controls noise with same level data 
           )


# ##### b. swarmplot

# In[7]:


sns.catplot(x='day',
            y='tip',
            data=data,
            kind='swarm'            
           )
# can also use sns.swarmplot(x='day',y='tip',data=data)


# In[8]:


sns.catplot(x='day',
            y='tip',
            data=data,
            kind='swarm',
            hue='sex'       
           )


# ### 2. categorical distribution plots

# ##### a. box-plot 

# In[9]:


sns.boxplot(data['tip'])


# In[10]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='box'
           )


# In[11]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='box',
            hue='sex'
            )


# ##### b. violin-plot(boxplot + PDF)

# In[12]:


sns.violinplot(data['tip'])


# In[13]:


sns.violinplot(data['total_bill'])


# In[14]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='violin',
           )


# In[15]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='violin',
            hue='sex'
           )


# In[16]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='violin',
            hue='sex',
            split=True
           )


# ### 3. categorical estimate plots

# ##### a. Point-plot 

# In[17]:


sns.pointplot(data['total_bill'])


# In[18]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='point'
           )


# In[19]:


sns.catplot(x='day',
            y='total_bill',
            data=data,
            kind='point',
            hue='sex'
           )


# ##### b. bar-plot

# In[43]:


sns.barplot(x='smoker',
            y='total_bill',
            data=data,
           )


# In[21]:


sns.catplot(x='smoker',
            y='total_bill',
            data=data,
            kind='bar',
            hue='sex'
           )


# In[22]:


sns.catplot(x='smoker',
            y='total_bill',
            data=data,
            kind='bar',
            hue='sex',
            estimator=np.var #default value is np.value
           )


# ##### c. count-plot ~ histogram

# In[23]:


sns.countplot(data['sex'])


# In[24]:


sns.catplot(x='sex',
              data=data,
              kind='count',
              hue='smoker'
             )


# ### 4. categorical categorical plots

# ##### a. Heat-maps

# In[25]:


flights=sns.load_dataset('flights')


# In[26]:


flights.shape


# In[27]:


flights.head()


# In[28]:


x=flights.pivot_table(index='year',columns='month',values='passengers',aggfunc='sum')


# In[29]:


sns.heatmap(x)


# In[30]:


sns.heatmap(x,cbar=False) #color gets off


# In[31]:


sns.heatmap(x,cbar=True,linewidths=2) #line width within color cell


# In[32]:


sns.heatmap(x,
            cbar=True,
            linewidths=2,
            linecolor='m'
           ) #line color in width replace within color cell


# In[33]:


sns.heatmap(x,
            cbar=True,
            linewidths=2.5,
            linecolor='k',
            annot=True
           )


# In[34]:


sns.heatmap(x,
            cbar=True,
            linewidths=2,
            linecolor='k',
            annot=True,
            fmt='d'
           )


# In[35]:


sns.heatmap(x,
            cbar=True,
            linewidths=2,
            cmap='viridis'
           )


# In[36]:


sns.heatmap(x,
            cbar=True,
            linewidths=2,
            cmap='summer'
           )


# In[37]:


sns.heatmap(x,
            cbar=True,
            linewidths=2,
            cmap='winter'
           )


# ##### b. cluster-maps

# In[38]:


sns.clustermap(x)


# In[39]:


#all parameter used in heatmap is similar
# and for clustering it uses metric : euclidian dist


# In[40]:


sns.clustermap(x,
              metric='correlation'
              )


# In[41]:


sns.clustermap(x,
               metric='correlation',
               z_score=0,
               annot=True
              )


# In[42]:


sns.clustermap(x,
               metric='correlation',
               z_score=0,
               annot=True,
               row_cluster=False# similar to colomn cluster
              )


# In[44]:


data


# In[46]:


sns.heatmap(data.corr())


# In[ ]:




