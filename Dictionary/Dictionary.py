#!/usr/bin/env python
# coding: utf-8

# In[5]:


thisdict = { "year": 1964,"brand": "Ford","model": "Mustang", "year": 2020 }
thisdict["year"] = 2021
print(thisdict["year"])


# #### Create a dictionary of student attribute

# In[6]:


record = dict()
record = {"Name" : "Muhammad Yasir", "Roll No" : "BITF19M526", "degree" : "Bs - IT", "semester" : 5}

print(record)
print(record['Name'])
print(len(record))

print("Roll No" in record)
print("Roll no" in record)

#print(record["Muhammad Yasir"]) #Direct data can not be accessed
val = record.values()
print(val)
print("Muhammad Yasir" in val)
print("Muhammad yasir" in val)


# #### Count Character using dictionary

# In[7]:


word = "Muhammad Yasir Babar"
d = dict()

for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1 
        
print(d)


# #### Count number of words in a file and check if a certain word exist in file, else show 0

# In[8]:


fout = open("data.txt")

count = dict()

for line in fout:
    words = line.split() #will create a list of all words (sepreated by a space)
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

#print(count)
for key in count:
    print(key, count[key], end = "\t")

val = input("\nEnter word to find ")
print(count.get(val, 0))


# #### Display count of words in sorted order

# In[9]:


li = list(count.keys())
li.sort()
for key in li:
    print(key, count[key])

