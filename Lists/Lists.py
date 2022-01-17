#!/usr/bin/env python
# coding: utf-8

# In[10]:


li = [1,2,3,4,5,5]
print(li[0])
li[0] = 90
print(li[0])


# In[12]:


li =(1,2,3,5,5)
print(li[0])

#li[0] = 90

print(li[0])


# In[27]:


di = dict()
di = {"m": 0, "y" : 1, "by": 2}

print(di['by'])


# #### Write a program that lets the user to enter the marks of 10 quizzes of a student into an array of integers. The program should calculate and display the total of all the student’s quizzes.

# In[4]:


def sum_marks():
    marks = []
    for i in range(10):
        marks.append(int(input("Enter Marks of student %d : " %(i+1))))
        
    print("Sum of marks = ", sum(marks))
    
sum_marks()


# #### Write a program that lets the user enter the total rainfall for each of 12 months into an array of doubles. The program should display the month having highest rainfall in the year.

# In[8]:


def rainfall():
    rain = []
    for i in range(12):
        rain.append(float(input("Enter Rain for month %d : " %(i+1))))
        
    print("Highest Rainfall was in ", max(rain))
    
rainfall()


# #### Write a program that lets the user to enter 10 integers into an array. The program should add pairs of elements together, starting with elements at index 0 with 1, 2 with 3, 4 with 5 and so on. Save all the results into a separate array and display the values of resulting array. 
# 

# In[11]:


def data():
    rec = []
    for i in range(10):
        val = int(input("Enter Value %d : " %(i+1)))
        rec.append(val)
    
    return rec

def add():
    rec = data()
    
    sum = []
    for i in range(0, len(rec), 2):
        sum.append(rec[i] + rec[i+1])
        
    print("\nAlternative value sum list is : ",sum)
    
add()


# #### The local Driver’s License Office has asked you to write a program that grades the written portion of the driver’s license exam. The exam has 10 multiple choice questions.
# ##### Here are the correct answers:
# #### Question 1 2 3 4 5 6 7 8 9 10
# #### Answer 4 1 2 1 3 2 1 4 3 2
# Your program should store the correct answers shown above in an array. It should ask the user to enter the student’s answers for each of the 10 questions, and the answers should be stored in another array. After the student’s answers have been entered, the program should display a message indicating whether the student passed or failed the exam. A student must correctly answer 6 of the 10 questions to pass the exam. It should then display the
# #####  total number of correctly answered questions
# #####  total number of incorrectly answered questions
# ##### list showing the question numbers of the incorrectly answered questions. 

# In[19]:


def answers():
    ans = []
    for i in range(10):
        a = int(input("Enter answer for Q %d : " %(i+1)))
        ans.append(a)
    
    return ans

def result():
    key = [4,1,2,1,3,2,1,4,3,2]
    ans = answers()
    
    incorrect = []
    c1 = c2 = 0
    
    for i in range(10):
        if key[i] == ans[i]:
            c1 += 1
        else:
            c2 += 1
            incorrect.append(i)
            
    print("------------------------")
    print("Number of correct : ", c1)
    print("Number of incorrect : ", c2)
    print("List of incorrect one : ", incorrect)
    
result()

