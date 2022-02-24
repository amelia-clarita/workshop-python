#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = 12345, 54321, 'hello!'
t[0]


# In[2]:


t


# In[3]:


# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u


# In[4]:


# Tuples are immutable:
t[0] = 88888


# In[5]:


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v


# In[6]:


empty = ()
singleton = 'hello',    # <-- note trailing comma
len(empty)


# In[7]:


len(singleton)


# In[8]:


singleton


# In[9]:


x, y, z = t


# In[ ]:




