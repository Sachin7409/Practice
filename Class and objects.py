#!/usr/bin/env python
# coding: utf-8

# * In python everything is an object. we can check this as well
# * Everything in Python is an object, and almost everything has attributes and methods. All functions have a built-in attribute __doc__, which returns the docstring defined in the function source code

# In[1]:


a = 1
b ='Sachin'
c = 3.3
d = [1,2,3,'Sachin','Kushal','Arnav','Sachin']
e = (10,11,22,'Raghavendra','Pavan','Arun',22)
f = {1,2,3,2}
g = {1:2,2:'Sachin',3:[32,6.7]}


# In[2]:


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


# As we can see everything is an object of their respective class.
# 
# 
# Classes -- Template
# 
# Object -- Particuar instance of that Template
# 
# 
# Example 1. -- **Certificate**
# 
# 1. Here certififcate is a class and company wants to give certificates to 1000 learners who completed their course.
# 2. what company will do is they just prepare a template of certificate first. Then thwy have to do one thing only.
# 3. they will just write the student name, start date and compeltion date.
# 4. Now the company will provide the certificate to learners. They do not write whole certificate for each and every learner again and again. 
# 4. All the certificates will be counted as object ofcertificate class or template.
# 
# Example 2.  -- **Movie script**
# 
# 1. there is a movie script for a movie.
# 2. Now the director shoots the movie.
# 3. shooting is an object of that script. because director ha to take many shots for one scene. If he has not prepare the script first then he has to write script again and again for each take.
# 3. So script is written already he can take as many takes for one scene. All the scenes will be cout as an object.

# In[3]:


class Employee:
    pass


# In the above code I have not prepared full template or class i just created a class Employee because in my mind there is no attributes or code present but I need to keep this name in my mind so i just created and write **pass** statement inside class, if i did not wrote **pass** there then it will throw me error. To avoid error I write **pass**

# In[4]:


class Employee:
    pass 
    
arun = Employee()   # I created one instance here
sai = Employee()     # second instance 
# there is one object called Employee
# now arun and sai are two instance objects of Employee object of class Employee.


# # Points to remember
# ####  A class provides the blueprint for objects.
# #### We creates an object and assigns it to a variable.
# #### When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.
# ####  When you create an object, you are creating an instance of a class

# # Class    ----> Template or Design
# ![image.png](attachment:image.png)

# # Object  ----> Instance or Prototype
# ![image.png](attachment:image.png)

# For example I am a Builder and I construct buildings, houses, villa and many more. So I have 10 clients who wants me to build houses for them. First thing what I will do is I wil prepare one design first and according to that design I will build homes for all the 10 clients.
# 
# 1. House design ------------ 1 class or Template
# 2. 10 houses of clients ---- 10 objects

# ### Now we will create our own data type and class and method as well
# ### When we define a class, it needs to create an object to allocate the memory

# In[3]:


class cat:
    name = ''
    age = 0
    color = ''
    
    # I will create def __init__ which is a default constructor and pass the self parameter first
    # which will reference the current object
    
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')
        
    # Now I will define some real methods 
    
    def meow(self):
        print(f'{self.name} meow meow')
    
    def hungry(self):
        for x in range(5):
            self.meow()
    
    def sleep(self):
        print(f'{self.name} zzzphuuhhhzzz')
        
    def about(self):
        print(f'{self.name} is {self.age} years old and its colur is {self.color}')
        
        
a = cat('Kitty',2,'Cream')


# So now our class is not doing more things here because i just created an instance only
# Now i will use this class in some other program by importing it
# 

# In[ ]:





# In[ ]:





# In[ ]:




