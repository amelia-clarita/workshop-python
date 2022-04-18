#!/usr/bin/env python
# coding: utf-8

# In[1]:


import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)


# In[2]:


a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive


# In[3]:


del a                       # remove the one reference
gc.collect()                # run garbage collection right away


# In[4]:


d['primary']                # entry was automatically removed


# In[ ]:




