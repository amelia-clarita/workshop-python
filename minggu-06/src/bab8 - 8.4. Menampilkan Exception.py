#!/usr/bin/env python
# coding: utf-8

# In[1]:


raise NameError('HiThere')


# In[2]:


raise ValueError  # shorthand for 'raise ValueError()'


# In[3]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# In[ ]:




