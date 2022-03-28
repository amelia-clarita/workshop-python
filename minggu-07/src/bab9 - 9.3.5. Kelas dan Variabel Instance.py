#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


# In[2]:


d = Dog('Fido')


# In[3]:


e = Dog('Buddy')


# In[4]:


d.kind                  # shared by all dogs


# In[5]:


e.kind                  # shared by all dogs


# In[6]:


d.name                  # unique to d


# In[7]:


e.name                  # unique to e


# In[8]:


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[9]:


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs


# In[10]:


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


# In[11]:


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks


# In[12]:


e.tricks


# In[ ]:




