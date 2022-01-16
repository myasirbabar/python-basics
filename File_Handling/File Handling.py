#!/usr/bin/env python
# coding: utf-8

# In[9]:


def open_file():
    fout = open("rec.txt")
    for line in fout:
        print(line)

def write_file():
    fout = open("rec.txt", 'w')
    fout.write("my name is blah blah ")

write_file()
open_file()


# ### Writing a .txt file

# In[1]:


def data(n):
    print("Enter Data for Student : ", i + 1)
    
    rollno = input("Enter Your Roll no : ")
    name = input("Enter Your Name : ")
    
    if "it" in rollno.lower():
        deg = "BS - IT"
        
    elif "cs" in rollno.lower():
        deg = "BS - CS"
    
    elif "se" in rollno.lower():
        deg = "BS - SE"
    
    sem = input("Enter Your semester : ")
    password = "pucit"
    email = rollno + "@pucit.edu.pk"
    
    print("------------------------")
    
    write(rollno, name, deg, sem, password, email)
    
def write(r,n,d,s,p,e):
    fout = open("record.txt", 'a')
    line = r + "\t" + n + "\t" + d + "\t" + s + "\t" + p + "\t" + e + "\n"
    fout.write(line)
    
    fout.close

n = int(input("Enter Number Of records : "))
print()

for i in range(n):
    try:
        data(i)
    except:
        print("Error In writing File")

print("Data Entered Successfully")


# ### Writing a .csv File

# In[3]:


#SAME CODE FOR INPUT AS IN .TXT FILE
    
def write(r,n,d,s,p,e):
    fout = open("record.csv", 'a')
    
    #JUST REPLACE TABS WITH COMAS
    line = r + "," + n + "," + d + "," + s + "," + p + "," + e + "\n"
    fout.write(line)
    
    fout.close

n = int(input("Enter Number Of records : "))
print()

for i in range(n):
    try:
        data(i)
    except:
        print("Error In writing File")

print("Data Entered Successfully")


# ### Reading a .txt File

# In[2]:


def read():
    try:
        file = open("record.txt")
    except:
        print("File Not Found")
        exit()
        
    count = 1
    for line in file:
        print("Student ", count)
        print(line)
        count += 1
        
read()


# ### Reading a .csv File

# In[8]:


def read():
    try:
        file = open("record.csv")
    except:
        print("File Not Found")
        exit()
        
    count = 0
    for line in file:
        
        if count == 0:
            count += 1
            continue
            
        print("Student ", count)
        newline = ""
        
        for i in range(len(line)):
            if line[i] == ',':
                newline += "\t"
                continue
                
            newline += line[i]
            
        print(newline)
        count += 1
        
read()

