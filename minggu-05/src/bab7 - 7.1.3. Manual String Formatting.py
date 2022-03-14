#!/usr/bin/env python
# coding: utf-8

# In[1]:


for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


# In[2]:


'12'.zfill(5)


# In[3]:


'-3.14'.zfill(7)


# In[4]:


'3.14159265359'.zfill(5)


# In[ ]:




