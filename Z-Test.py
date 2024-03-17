#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to implement One Sample Z-Test


# In[2]:


# Importing the required libraries
import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests


# In[3]:


# Creating a dataset
data = [89, 93, 95, 93, 97, 98, 96, 99, 93, 97,
110, 104, 119, 105, 104, 110, 110, 112, 115, 114]


# In[4]:


# Performing the z-test
z_test ,p_val = stests.ztest(data, x2 = None, value = 160)
print(p_val)


# In[5]:


# taking the threshold value as 0.05 or 5%
if p_val < 0.05:
    print("We can reject the null hypothesis")
else:
    print("We can accept the null hypothesis")


# In[ ]:




