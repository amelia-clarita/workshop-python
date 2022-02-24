#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves


# In[2]:


queue.popleft()                 # The second to arrive now leaves


# In[3]:


queue                           # Remaining queue in order of arrival


# In[ ]:




