#!/usr/bin/env python
# coding: utf-8

# In[1]:


tel = {'jack': 4098, 'sape': 4139}


# In[2]:


tel['guido'] = 4127


# In[3]:


tel


# In[4]:


tel['jack']


# In[5]:


del tel['sape']


# In[6]:


tel['irv'] = 4127


# In[7]:


tel


# In[8]:


list(tel)


# In[9]:


sorted(tel)


# In[10]:


'guido' in tel


# In[11]:


'jack' not in tel


# In[12]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[13]:


{x: x**2 for x in (2, 4, 6)}


# In[14]:


dict(sape=4139, guido=4127, jack=4098)


# In[ ]:




