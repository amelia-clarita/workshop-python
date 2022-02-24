#!/usr/bin/env python
# coding: utf-8

# In[1]:


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


# In[2]:


[[row[i] for row in matrix] for i in range(4)]


# In[3]:


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])


# In[4]:


transposed


# In[5]:


transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)


# In[6]:


transposed


# In[7]:


list(zip(*matrix))


# In[ ]:




