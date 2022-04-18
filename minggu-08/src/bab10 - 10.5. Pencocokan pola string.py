#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[2]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[3]:


'tea for too'.replace('too', 'two')


# In[ ]:




