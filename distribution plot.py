#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns


# In[2]:


plt.style.use('fivethirtyeight')


# In[3]:


titanic=sns.load_dataset('titanic')


# In[4]:


titanic.shape


# In[5]:


titanic.head()


# In[6]:


titanic['age'].fillna(titanic['age'].mean(),inplace=True)


# ## displot

# In[7]:


sns.displot(titanic['age'],
            color='c',
            alpha=0.7,)


# In[11]:


sns.distplot(titanic['age'],kde=False)


# In[13]:


sns.distplot(titanic['age'],
             kde=False,
             bins=100
            )


# ## KDE/PDF

# In[14]:


sns.distplot(titanic['age'],
             kde=True,
             hist=False
            )


# ## rugplot

# In[20]:


sns.distplot(titanic['age'],
             kde=False,
             hist=False,
             rug=True,
             bins=10
            )


# ## distplot

# In[8]:


sns.distplot(titanic['age'])


# In[12]:


sns.distplot(titanic[titanic['survived']==1]['age'])
sns.distplot(titanic[titanic['survived']==0]['age'])


# In[19]:


sns.distplot(titanic[titanic['survived']==1]['age'])


# In[ ]:




