#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum(i*i for i in range(10))                 # sum of squares


# In[2]:


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))         # dot product


# In[4]:


unique_words = set(word for line in page  for word in line.split())


# In[5]:


valedictorian = max((student.gpa, student.name) for student in graduates)


# In[6]:


data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))


# In[ ]:




