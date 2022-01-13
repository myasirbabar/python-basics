#!/usr/bin/env python
# coding: utf-8

# #### Write an if-else statement that outputs the word “High” if the value of the variable score is greater than 100, and “Low” if the value of score is at most 100. 

# In[8]:


value = int(input("Enter A Value : "))
if value > 100 :
    print("High")
else :
    print("Low")


# #### Write a program that gets a number from user, if it is negative then display “The number is negative” otherwise,  display “The number is non-negative”. 

# In[ ]:


value = input("Enter a Number : ")
if int(value) < 0 :
    print("The Number is negative")
else :
    print("The Number is positive")


# #### Prompt the user for two numbers A & B, computes and displays C=A/B. If the number B is zero, displays a “division by Zero” message. 

# In[11]:


A = input("Enter Number A : ")
B = input("Enter Number B : ")

if int(B) == 0 :
    print("Division By zero Error !")
else :
    C = int(A) / int(B)
    print(int(C))


# #### Input two positive numbers from user and display the maximum out of them.  

# In[ ]:


A = input("Enter Number A : ")
B = input("Enter Number B : ")

if int(A) < 0 or int(B) < 0 :
    print("Both Numbers Should Be Positive")
else :
    if(A >= B) :
        print(A)
    else :
        print(B)
    #print(max(A,B))


# #### Three numbers denoted by the variables A, B and C are supplied as input data. Identify and print the largest one of these numbers. 

# In[ ]:


A = input("Enter Number A : ")
B = input("Enter Number B : ")
C = input("Enter Number C : ")

if A > B and A > C :
    print(A)
elif B > A and B > C :
    print(B)
else :
    print(C)
#print(max(A,B,C))


# #### Write a program that reads an integer and determines and prints whether it is odd or even. (Hint: First use the simple division, then introduce modulus operator)

# In[ ]:


value = int(input("Enter an integer : "))
if value % 2 == 0 :
    print("Even")
else :
    print("Odd")


# #### Write a program that reads two integers (in any order) and then print either “multiple” or “not” according to weather 2nd number is multiple of the 1st one or not. 

# In[ ]:


A = int(input("Enter A integer : "))
B = int(input("Enter B integer : "))

if B % A == 0 :
    print("Multiple")
else :
    print("Not Multiple")


# #### Write a program that gives absolute of a number input by user

# In[ ]:


val = int(input("Enter a number : "))
if val < 0:
    val *= -1

print(val)


# #### Write a program that requests an integer value representing the month of the year and gives the number of days in that month.  

# In[ ]:


val = int(input("Enter Month : "))
if val == 2:
    print("28")
else :
    if val < 8 :
        if val % 2 == 0:
            print("30")
        else :
            print("31")
    else :
        if val % 2 != 0:
            print("30")
        else :
            print("31")


# #### Write a program that reads a single digit value (0-9) and then prints the number as a literal string. For example, if input is 7, then the output should be word “seven”.

# In[ ]:


val = int(input("Enter Digit : "))
if val > 9 :
    print("Enter Value in between 0 -- 9 ")
else :
    array = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    index = 0
    for st in array:
        if val == index:
            print(st)
        index += 1


# #### Write a program that inputs a number and displays its number of digits. Assume that user will enter a positive number less than 1000.

# In[ ]:


val = int(input("Enter An Integer : "))

if val >= 1000 or val < 0:
    print("Data Not Valid")

else :
    if val >= 0 and val < 10 :
        print("1")
    if val >= 10 and val < 100 :
        print("2")
    if val >= 100 and val < 999 :
        print("3")

