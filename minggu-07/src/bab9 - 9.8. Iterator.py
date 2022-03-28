#!/usr/bin/env python
# coding: utf-8

# In[1]:


for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


# In[2]:


s = 'abc'
it = iter(s)
it


# In[3]:


next(it)


# In[4]:


next(it)


# In[5]:


next(it)


# In[6]:


next(it)


# In[7]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[8]:


rev = Reverse('spam')
iter(rev)


# In[9]:


for char in rev:
    print(char)


# In[ ]:




