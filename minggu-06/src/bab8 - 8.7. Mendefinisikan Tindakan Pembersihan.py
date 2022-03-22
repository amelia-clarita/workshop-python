#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# In[2]:


def bool_return():
    try:
        return True
    finally:
        return False


# In[3]:


bool_return()


# In[4]:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


# In[5]:


divide(2, 1)


# In[6]:


divide(2, 0)


# In[7]:


divide("2", "1")


# In[ ]:




