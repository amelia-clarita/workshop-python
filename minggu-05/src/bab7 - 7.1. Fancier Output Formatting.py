#!/usr/bin/env python
# coding: utf-8

# In[1]:


year = 2016


# In[2]:


event = 'Referendum'


# In[3]:


f'Results of the {year} {event}'


# In[4]:


yes_votes = 42_572_654


# In[5]:


no_votes = 43_132_495


# In[6]:


percentage = yes_votes / (yes_votes + no_votes)


# In[7]:


'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)


# In[8]:


s = 'Hello, world.'
str(s)


# In[9]:


s = 'Hello, world.'
str(s)


# In[10]:


str(1/7)


# In[11]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# In[12]:


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)


# In[13]:


# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))


# In[ ]:




