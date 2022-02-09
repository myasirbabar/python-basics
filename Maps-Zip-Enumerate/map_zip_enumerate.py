#!/usr/bin/env python
# coding: utf-8

# # MAP

# ### Given a list find numbers of letters in each value of list using map

# In[3]:


def letters(n):
    return len(n)

li = ["Muhammad", "Yasir", "Babar", "Bhatti"]
x = map(letters, li) #Map automatically call letter function with each value of li and store result in x. 

print(list(x)) #Displayed count in list form


# ### Concatenate two strings using map

# In[5]:


def concate(a,b):
    return a + " " + b

f = ["Muhammad", "Zaheer", "Altaf"]
l = ["Yasir", "Babar", "Hussain"]

x = map(concate, f,l)

print(list(x))


# # ZIP

# ### Concatenate names using zip

# In[11]:


# concate function is not req if we use zip for performing this task

f = ["Muhammad", "Zaheer", "Altaf"]
l = ["Yasir", "Babar", "Hussain"]

x = zip(f,l)

print(list(x))    


# # Enumerate

# In[12]:


# Assigning IDS to values is called enumerating

f = ["Muhammad", "Zaheer", "Altaf"]
ID = enumerate(f)

for i in ID:
    print(i)

