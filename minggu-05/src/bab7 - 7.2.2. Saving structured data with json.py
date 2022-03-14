#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
x = [1, 'simple', 'list']
json.dumps(x)


# In[2]:


json.dump(x, f)


# In[3]:


x = json.load(f)


# In[ ]:




