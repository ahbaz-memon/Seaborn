#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# In[2]:


plt.style.use('fivethirtyeight')#styling for beauty


# In[3]:


data=sns.load_dataset('tips')


# In[4]:


data.head()


# In[5]:


sns.relplot(x='total_bill',
            y='tip',
            data=data,
            kind='scatter')


# In[6]:


sns.relplot(x='total_bill',
            y='tip',
            data=data,
            kind='scatter',
            style='smoker')


# In[7]:


sns.relplot(x='total_bill',
           y='tip',
           data=data,
           kind='scatter',
           hue='sex',
           style='smoker')


# In[8]:


sns.relplot(x='total_bill',
           y='tip',
           data=data,
           kind='scatter',
           hue='sex',
           style='smoker',
           size='size')#can increase size by sizes=(min,max)


# In[9]:


sns.scatterplot(x='total_bill',
            y='tip',
            data=data,
            hue='sex',
            style='smoker',
            size='size')

