#!/usr/bin/env python
# coding: utf-8

# ## Theoretical Question

# Q1. super(childClassName, self)._init_()
# 
# Q3. people = {1: {'name': 'Sahil', 'age': '21', 'sex': 'Male'},
#           2: {'name': 'Shikha', 'age': '22', 'sex': 'Female'}}
# 
# print(people)
# 
# Q2. class Parent:
#      pass
# class Child(Parent):
#      pass
#      
#   Here the class child inherits the class parent
# 

# ## programming Questions

# ## SetB Q1

# In[1]:


phrase = input("Please enter your sentence here: ")
phrase_splited = phrase.split(' ')

word_list = []
for i in phrase_splited:
    if i not in word_list:
        word_list.append(i)
    else:
        continue
word_list.sort()
print((' ').join(word_list))


# ## Set B Q2

# In[2]:


#the value 24 in
list1 = [12,24,35,24,88,120,155]  
list1 = [ elem for elem in list1 if elem != 24] 
print(*list1)


# In[ ]:




