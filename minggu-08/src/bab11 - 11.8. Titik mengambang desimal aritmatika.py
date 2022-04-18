#!/usr/bin/env python
# coding: utf-8

# In[1]:


from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)


# In[2]:


round(.70 * 1.05, 2)


# In[3]:


Decimal('1.00') % Decimal('.10')


# In[4]:


1.00 % 0.10


# In[5]:


sum([Decimal('0.1')]*10) == Decimal('1.0')


# In[6]:


sum([0.1]*10) == 1.0


# In[7]:


getcontext().prec = 36
Decimal(1) / Decimal(7)


# In[ ]:




