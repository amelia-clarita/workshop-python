#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n): #write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[2]:


# Now call the function we just defined:
fib(2000)


# In[3]:


fib


# In[4]:


f = fib


# In[5]:


f(100)


# In[6]:


fib(0)


# In[7]:


print(fib(0))


# In[8]:


def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result


# In[9]:


f100 = fib2(100) #call it


# In[10]:


f100            #write the result


# In[11]:


print("4.8.1 Default Argument Values")


# In[12]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[13]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[14]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[15]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[16]:


print("4.8.2 Keyword Arguments")


# In[17]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[18]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[19]:


parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# In[20]:


def function(a):
    pass


# In[21]:


function(0, a=0)


# In[22]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[23]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[25]:


print("4.8.3 Special Parameters")


# In[26]:


def standard_arg(arg):
    print(arg)


# In[27]:


def pos_only_arg(arg, /):
    print(arg)


# In[28]:


def kwd_only_arg(*, arg):
    print(arg)


# In[38]:


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# In[30]:


standard_arg(2)


# In[31]:


standard_arg(arg=2)


# In[32]:


pos_only_arg(1)


# In[39]:


pos_only_arg(arg=1)


# In[34]:


kwd_only_arg(3)


# In[35]:


kwd_only_arg(arg=3)


# In[36]:


combined_example(1, 2, 3)


# In[40]:


combined_example(1, 2, kwd_only=3)


# In[41]:


combined_example(1, standard=2, kwd_only=3)


# In[42]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[43]:


def foo(name, **kwds):
    return 'name' in kwds


# In[44]:


foo(1, **{'name': 2})


# In[45]:


def foo(name, /, **kwds):
    return 'name' in kwds


# In[46]:


foo(1, **{'name': 2})


# In[59]:


print("4.8.4 Arbitrary Argument Lists")


# In[58]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[49]:


def concat(*args, sep="/"):
    return sep.join(args)


# In[50]:


concat("earth","mars","venus")


# In[51]:


concat("earth", "mars", "venus", sep=".")


# In[60]:


print("4.8.5 Unpacking Arguments Lists")


# In[52]:


list(range(3, 6))            # normal call with separate arguments


# In[53]:


args = [3, 6]


# In[55]:


list(range(*args)) # call with arguments unpacked from a list


# In[56]:


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# In[57]:


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[61]:


print("4.8.6 Lambda Expressions")


# In[62]:


def make_incrementor(n):
    return lambda x: x + n


# In[63]:


f = make_incrementor(42)
f(0)


# In[64]:


f(1)


# In[65]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# In[66]:


print("4.8.7 Documentation Strings")


# In[68]:


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


# In[69]:


print(my_function.__doc__)


# In[70]:


print("4.8.8 Function Annotations")


# In[71]:


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# In[72]:


f('spam')


# In[ ]:




