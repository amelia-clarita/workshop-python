#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Range() Function")


# In[2]:


for i in range(5):
    print (i)


# In[3]:


list(range(5, 10))


# In[4]:


list(range(0, 10, 3))


# In[5]:


list(range(-10, -100, -30))


# In[6]:


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])


# In[7]:


range(10)


# In[8]:


sum(range(4)) #0 + 1 + 2 + 3


# In[9]:


print("Break and Contine Statements, and Else Clauses on Loops")


# In[10]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')


# In[12]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found a even number", num)
        continue
    print("Found an odd number", num)


# In[ ]:




