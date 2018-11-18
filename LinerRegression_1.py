
# coding: utf-8

# In[1]:


#coding: UTF-8
from sklearn.linear_model import LinearRegression


# In[2]:


import pandas as pd


# In[3]:


stock_data = pd.read_csv('stockchart_20180908.csv')


# In[4]:


count_s =  len(stock_data)


# In[5]:


owarine = stock_data['終値'].values.tolist()


# In[ ]:





# In[6]:


owarine


# In[7]:


successive_data = []
answers = []
for i in range(4, count_s):
    successive_data.append([owarine[i-4], owarine[i-3], owarine[i-2], owarine[i-1]])
    answers.append(owarine[i] )


# In[8]:


reg = LinearRegression().fit(successive_data, answers)


# In[9]:


n = len(successive_data)
m = len(answers)


# In[10]:


n


# In[11]:


from sklearn import utils
utils.multiclass.type_of_target(answers)


# In[12]:


answers


# In[13]:


predicted = reg.predict(successive_data)


# In[14]:


predicted


# In[15]:


pd.Series(answers)


# In[16]:


c = pd.Series(answers)
d = pd.Series(predicted)


# In[17]:


e = pd.concat([c,d],axis=1)


# In[18]:


e.to_csv('result.csv')

