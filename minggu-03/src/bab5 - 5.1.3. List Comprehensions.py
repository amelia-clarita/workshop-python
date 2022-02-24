#!/usr/bin/env python
# coding: utf-8

# In[1]:


squares = []
for x in range(10):
    squares.append(x**2)


# In[2]:


squares


# In[3]:


squares = list(map(lambda x: x**2, range(10)))


# In[4]:


squares = [x**2 for x in range(10)]


# In[5]:


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


# In[6]:


combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))


# In[7]:


combs


# In[8]:


vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x*2 for x in vec]


# In[9]:


# filter the list to exclude negative numbers
[x for x in vec if x >= 0]


# In[10]:


# filter the list to exclude negative numbers
[x for x in vec if x >= 0]


# In[11]:


# apply a function to all the elements
[abs(x) for x in vec]


# In[12]:


# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]


# In[13]:


# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]


# In[14]:


# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]


# In[15]:


# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]


# In[16]:


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


# In[ ]:




