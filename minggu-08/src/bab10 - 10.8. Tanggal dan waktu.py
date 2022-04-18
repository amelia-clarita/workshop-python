#!/usr/bin/env python
# coding: utf-8

# In[1]:


# dates are easily constructed and formatted
from datetime import date
now = date.today()
now


# In[2]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[3]:


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days


# In[ ]:




