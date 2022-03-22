#!/usr/bin/env python
# coding: utf-8

# In[1]:


# exc must be exception instance or None.
raise RuntimeError from exc


# In[2]:


def func():
    raise ConnectionError


# In[3]:


try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


# In[4]:


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None


# In[ ]:




