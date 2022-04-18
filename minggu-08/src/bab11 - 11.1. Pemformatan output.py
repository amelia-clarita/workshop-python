#!/usr/bin/env python
# coding: utf-8

# In[1]:


import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))


# In[2]:


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]


# In[3]:


pprint.pprint(t, width=30)


# In[4]:


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""


# In[5]:


print(textwrap.fill(doc, width=40))


# In[6]:


import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')


# In[7]:


conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)


# In[8]:


locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)


# In[ ]:




