#!/usr/bin/env python
# coding: utf-8

# In[5]:


f.read()


# In[6]:


f.read()


# In[7]:


f.readline()


# In[8]:


f.readline()


# In[9]:


f.readline()


# In[10]:


for line in f:
    print(line, end='')


# In[11]:


f.write('This is a test\n')


# In[12]:


value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)


# In[13]:


f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')


# In[14]:


f.seek(5)      # Go to the 6th byte in the file


# In[15]:


f.read(1)


# In[16]:


f.seek(-3, 2)  # Go to the 3rd byte before the end


# In[17]:


f.read(1)


# In[ ]:




