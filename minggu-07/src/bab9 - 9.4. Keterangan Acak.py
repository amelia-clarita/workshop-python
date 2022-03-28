#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Warehouse:
    purpose = 'storage'
    region = 'west' 


# In[5]:


w1 = Warehouse()
print(w1.purpose, w1.region)


# In[6]:


w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


# In[7]:


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g


# In[8]:


class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)


# In[ ]:




