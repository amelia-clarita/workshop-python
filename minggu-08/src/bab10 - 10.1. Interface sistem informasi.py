#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()      # Return the current working directory


# In[2]:


os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell


# In[3]:


import os
dir(os)


# In[4]:


help(os)


# In[5]:


import shutil
shutil.copyfile('data.db', 'archive.db')


# In[6]:


shutil.move('/build/executables', 'installdir')


# In[ ]:




