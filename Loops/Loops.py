#!/usr/bin/env python
# coding: utf-8

# #### Finding the sum of 10 numbers taken from the user

# In[1]:


sum = 0
for x in range(0,10):
    val = int(input("Enter Value "))
    sum += val
    
print("Sum of Numbers = ", sum)


# ####  Finding the sum of n numbers taken from the user, where n is taken from the user as well. 

# In[2]:


n = int(input("Enter n "))
sum = 0
for x in range(n):
    val = int(input("Enter Value ")) 
    sum += val
    
print("Sum of ", n , " numbers = ", sum)


# #### Calculate the factorial of a positive integer entered by the user. 

# In[3]:


n = int(input("Enter n "))
fact = 1 #5! = 1.2.3.4.5
for x in range(1,n+1):
    fact *= x
    
print(n , "!  = ", fact)


# #### Take two positive integers a and n from the user. Calculate and display a n Assume that the power operator is not available.  

# In[ ]:


a = int(input("Input the value of a "))
n = int(input("Input the value of n "))
x = 1

for i in range(n):
    x *= a
    
print(a, "^", n, " = ", x)


# #### Take three numbers from the user and determine the largest number. Do it using a loop. 

# In[ ]:


a = int(input("Input the value of a "))
b = int(input("Input the value of b "))
c = int(input("Input the value of c "))

arr = [a,b,c]
lar = arr[0]
for i in range(1,3):
    if lar < arr[i]:
        lar = int(a[i])
        
print("Largest Number = ", lar)


# #### Take a positive integer from the user. Keep displaying an error message and prompting for input again and again if the user enters invalid input (negative or zero). 

# In[ ]:


while True :
    n = int(input("Input the number : "))
    if n > 0:
        break
    else:
        print("Incorrect Number. Enter Again")

print(n)


# #### Write an algorithm to determine the sum of a variable number of positive integers taken from the user. The algorithm should keep prompting the user for more input till the user enters the sentinel value -999. 

# In[ ]:


sum = 0
while True:
    val = int(input("Enter number : "))
    if val == -999:
        break
    sum += val
    
print("Sum = ", sum)


# #### Input a 2-digit number and find absolute difference between its digits. 

# In[ ]:


val = int(input("Enter a two - digit number "))

a = int(val / 10)
b = val - (a*10)

c = a - b

if c < 0 : 
    c *= -1
print("Difference is : ", c)


# #### Input SLimit and ELimit from user, and display Even numbers between range, with both limits included 

# In[ ]:


slimit = int(input("Enter Lower Limit "))
elimit = int(input("Enter upper Limit "))

for i in range(slimit, elimit+1):
    if i % 2 == 0:
        print (i)

