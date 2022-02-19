#!/usr/bin/env python
# coding: utf-8

# In[2]:


x = int(input("Please enter an integer: "))


# In[3]:


if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# In[4]:


print("For Statement")


# In[5]:


# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))


# In[6]:


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status


# In[ ]:




