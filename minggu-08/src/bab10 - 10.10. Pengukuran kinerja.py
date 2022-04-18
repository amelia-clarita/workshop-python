#!/usr/bin/env python
# coding: utf-8

# In[1]:


from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[2]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[ ]:




