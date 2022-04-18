#!/usr/bin/env python
# coding: utf-8

# In[1]:


import zlib
s = b'witch which has which witches wrist watch'
len(s)


# In[2]:


t = zlib.compress(s)
len(t)


# In[3]:


zlib.decompress(t)


# In[4]:


zlib.crc32(s)


# In[ ]:




