#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Tutorial Bab 2")


# In[4]:


the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")


# In[83]:


print("Tutorial Bab 3")


# In[5]:


print("Using python as a Calculator")


# In[6]:


2+2


# In[7]:


50 - 5*6


# In[8]:


(50 -  5*6) / 4


# In[9]:


8/5


# In[10]:


17 / 3 #classic division returns a float


# In[11]:


17 // 3 #floor division discards the fractional part


# In[12]:


17 % 3  # the % operator returns the remainder of the division


# In[13]:


5 * 3 + 2  # floored quotient * divisor + remainder


# In[14]:


5 ** 2  # 5 squared


# In[15]:


2 ** 7  # 2 to the power of 7


# In[16]:


width = 20
height = 5 * 9
width * height


# In[17]:


n  # try to access an undefined variable


# In[18]:


4 * 3.75 - 1


# In[19]:


tax = 12.5 / 100
price = 100.50
price * tax


# In[20]:


price + _


# In[21]:


round(_, 2)


# In[22]:


'spam eggs' # single quotes


# In[23]:


'doesn\'t' # using \' to escape the single quote...


# In[24]:


"doesn't" # ... or user double quotes instead


# In[25]:


'"Yes," they said.'


# In[26]:


"\"Yes,\" they said."


# In[27]:


'"Isn\'t," they said.'


# In[28]:


'"Isn\'t," they said.'

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output

print(s)  # with print(), \n produces a new line


# In[29]:


print('C:\some\name')  # here \n means newline!


print(r'C:\some\name')  # note the r before the quote


# In[30]:


print("""Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")


# In[31]:


# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'


# In[32]:


'Py' 'thon'


# In[33]:


text = ('Put several strings within parentheses '
        'to have them joined together.')
text


# In[41]:


prefix = 'Py'


# In[42]:


prefix + 'thon'


# In[44]:


word = 'Python'
word[0]  # character in position 0


# In[45]:


word[5]  # character in position 5


# In[46]:


word[-1] # last character


# In[47]:


word[-2] # second-last character


# In[48]:


word[-6]


# In[49]:


word[0:2]  # characters from position 0 (included) to 2 (excluded)


# In[50]:


word[2:5]  # characters from position 2 (included) to 5 (excluded)


# In[52]:


word[:2]   # character from the beginning to position 2 (excluded)


# In[53]:


word[4:]   # characters from position 4 (included) to the end


# In[54]:


word[-2:]  # characters from the second-last (included) to the end


# In[55]:


word[:2] + word[2:]


# In[56]:


word[:4] + word[4:]


# In[57]:


'J' + word[1:]


# In[58]:


word[:2] + 'py'


# In[59]:


s = 'supercalifragilisticexpialidocious'
len(s)


# In[60]:


squares = [1, 4, 9, 16, 25]
squares


# In[62]:


squares[0]


# In[63]:


squares[-1]


# In[64]:


squares[-3:]


# In[65]:


squares[:]


# In[66]:


squares + [36, 49, 64, 81, 100]


# In[67]:


cubes = [1, 8, 27, 65, 125]
4 ** 3


# In[69]:


cubes[3] = 64
cubes


# In[70]:


cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes


# In[71]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters


# In[72]:


# replace some values
letters[2:5] = ['C', 'D', 'E']
letters


# In[73]:


# now remove them
letters[2:5] = []
letters


# In[74]:


# clear the list by replacing all the elements with an empty list
letters[:] = []
letters


# In[75]:


letters = ['a', 'b', 'c', 'd']
len(letters)


# In[76]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x


# In[77]:


x[0]


# In[78]:


x[0][1]


# In[79]:


a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


# In[80]:


i = 256*256
print('The value of i is', i)


# In[81]:


a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b


# In[ ]:




