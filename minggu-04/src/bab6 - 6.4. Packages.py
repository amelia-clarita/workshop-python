#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sound.effects.echo


# In[2]:


sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)


# In[3]:


from sound.effects import echo


# In[4]:


echo.echofilter(input, output, delay=0.7, atten=4)


# In[5]:


from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)


# In[ ]:




