#!/usr/bin/env python
# coding: utf-8

# In[1]:


knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


# In[2]:


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)


# In[3]:


questions = ['name', 'quest', 'favorite color']


# In[4]:


answers = ['lancelot', 'the holy grail', 'blue']


# In[5]:


for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


# In[6]:


for i in reversed(range(1, 10, 2)):
    print(i)


# In[7]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)


# In[8]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']


# In[9]:


for f in sorted(set(basket)):
    print(f)


# In[10]:


import math


# In[11]:


raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]


# In[12]:


filtered_data = []


# In[13]:


for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)


# In[14]:


filtered_data


# In[ ]:




