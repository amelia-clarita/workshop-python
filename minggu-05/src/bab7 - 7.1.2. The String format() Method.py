#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('We are the {} who say "{}!"'.format('knights', 'Ni'))


# In[2]:


print('{0} and {1}'.format('spam', 'eggs'))


# In[3]:


print('{1} and {0}'.format('spam', 'eggs'))


# In[4]:


print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))


# In[6]:


print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))


# In[7]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))


# In[8]:


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# In[9]:


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# In[ ]:




