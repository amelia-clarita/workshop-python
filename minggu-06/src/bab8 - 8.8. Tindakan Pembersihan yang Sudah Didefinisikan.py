#!/usr/bin/env python
# coding: utf-8

# In[1]:


for line in open("myfile.txt"):
    print(line, end="")


# In[2]:


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# In[ ]:




