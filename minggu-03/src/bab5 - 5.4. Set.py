#!/usr/bin/env python
# coding: utf-8

# In[1]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed


# In[2]:


'orange' in basket                 # fast membership testing


# In[3]:


'crabgrass' in basket


# In[4]:


# Demonstrate set operations on unique letters from two words


# In[5]:


a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a


# In[6]:


a - b                              # letters in a but not in b


# In[7]:


a | b                              # letters in a or b or both


# In[8]:


a & b                              # letters in both a and b


# In[9]:


a ^ b                              # letters in a or b but not both


# In[11]:


a = {x for x in 'abracadabra' if x not in 'abc'}


# In[12]:


a


# In[ ]:




