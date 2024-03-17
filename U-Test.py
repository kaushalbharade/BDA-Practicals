#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to implement Mann-Whitney U Test
# Importing the required dataset
from scipy.stats import mannwhitneyu


# In[2]:


# Creating the dataset
data1 = [10,20,30,40,50,66,55,34,54,39]
data2 = [33,45,67,87,98,44,33,98,70,90]


# In[3]:


# Implementing the test
k_test, p_val = mannwhitneyu(data1, data2)
print("P-value is: ", p_val)


# In[4]:


# taking the threshold value as 0.05 or 5%
if p_val < 0.05:
    print(" We can reject the null hypothesis")
else:
    print("We can accept the null hypothesis")


# In[ ]:




