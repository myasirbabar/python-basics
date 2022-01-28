#!/usr/bin/env python
# coding: utf-8

# # Classes and Objects in Python

# In[12]:


class student(object):
    
    # DEFINE CTOR
    def __init__(self, name, rollno,sem, deg, password):
        
        # self ==> this pointer
        self.name = name
        self.rollno = rollno
        self.sem = sem
        self.deg = deg
        self.password = password
        self.email = rollno + "@pucit.edu.pk"
        
    #GETTERS
    def get_rollno(self):
        return self.rollno
    
    def get_email(self):
        return self.email
    
    def set_name(self, name):
        self.name = name
    
    

# CRAETING AN OBJECT OF CLASS STUDENT
s1 = student("Myb", "bitf19m526", 5, "BS - IT", "pucit")


#ACCESSING MEMBERS DIRECTLY AND THROUGH GETTERS
print(s1.rollno)
print(s1.get_rollno())

print()

print(s1.email)
print(s1.get_email())

print()


#UPDATING MEMBERS DIRECTLY AND THROUGH SETTERS
s1.name = "Muhammad Yasir"
print(s1.name)

s1.set_name("Muhammad Yasir Babar")
print(s1.name)

print()

#CREATING A DATA MEMBER AT RUNTIME
mark_list = {"English":87, "Urdu": 50}
s1.marks = mark_list
print(s1.marks)

