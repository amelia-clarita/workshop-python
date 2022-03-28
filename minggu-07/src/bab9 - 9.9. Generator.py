#!/usr/bin/env python
# coding: utf-8

# In[1]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[2]:


for char in reverse('golf'):
    print(char)


# In[ ]:




