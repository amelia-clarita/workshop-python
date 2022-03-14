#!/usr/bin/env python
# coding: utf-8

# In[1]:


f = open('workfile', 'w')


# In[2]:


with open('workfile') as f:
    read_data = f.read


# In[3]:


# We can check that the file has been automatically closed.
f.closed


# In[4]:


f.close()
f.read()


# In[ ]:




