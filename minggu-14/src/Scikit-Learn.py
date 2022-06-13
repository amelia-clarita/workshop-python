#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets


# In[2]:


iris = datasets.load_iris()


# In[3]:


digits = datasets.load_digits()


# In[4]:


print(digits.data)


# In[5]:


digits.target


# In[6]:


digits.images[0]


# In[7]:


from sklearn import svm


# In[12]:


clf = svm.SVC(gamma=0.001, C=100.)


# In[13]:


clf.fit(digits.data[:-1], digits.target[:-1])


# In[14]:


clf.predict(digits.data[-1:])


# In[15]:


import numpy as np
from sklearn import kernel_approximation


# In[16]:


rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype


# In[17]:


transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype


# In[18]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


# In[19]:


list(clf.predict(iris.data[:3]))


# In[20]:


clf.fit(iris.data, iris.target_names[iris.target])


# In[21]:


list(clf.predict(iris.data[:3]))


# In[22]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)


# In[23]:


clf = SVC()
clf.set_params(kernel='linear').fit(X, y)


# In[24]:


clf.predict(X[:5])


# In[25]:


clf.set_params(kernel='rbf').fit(X, y)


# In[26]:


clf.predict(X[:5])


# In[27]:


from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer


# In[28]:


X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]


# In[29]:


classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X, y).predict(X)


# In[30]:


y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[31]:


from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[ ]:




