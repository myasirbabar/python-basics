#!/usr/bin/env python
# coding: utf-8

# ### Lamda is a small anonumus function 

# Syntax: 
# 
# lambda args : expression

# In[2]:


sum = lambda a,b:a+b # takes 2 args a, b perform a+b and return 

print(sum(5,6))


# ### A function returning a lambda function

# In[3]:


def unknown(a):
    return lambda b:b*a

mylambda = unknown(5) # Now in mylambda Lambda function will be saved i.e lambda b:b*5

print(mylambda(10)) # now this is calling lambda function i.e args = b = 10 and will return b*5 = 10 *5 = 50

