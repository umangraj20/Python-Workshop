#Q1 Write a Python program to create a tuple.

var1=(1,"c",False)
print(var1)

#Q3 Write a Python program to create a tuple with numbers and print one item.
var2=(1,4,7)
print(var2[2])

#Q4 Write a Python program to unpack a tuple in several variables.
var1=(10,30,40)
c,d,e=var1
print(c,d,e)

#Q5 Write a Python program to add an item in a tuple.
var1=(10,20,30)
var1=var1+(60,)
print(var1)

#Q6 Write a Python program to convert a tuple to a string.
var1=("a","b","c")
str=' ' .join (var1)
print(str)

#Q7 Write a Python program to get the 4th element and 4th element from last of a tuple
var1=(1,2,3,4,5,6,7,8,9,10)
print(var1[5],var1[-4])

#Q8 Write a Python program to create the colon of a tuple
var1=("a","b","c","d","e","f","g","h")
print(var1[5],var1[-4])

#Q9 Write a Python program to find the repeated items of a tuple
var1=(1,1,2,3)
count=(var1).count(1)
print(count)

#Q10 Write a Python program to check whether an element exists within a tuple
var1=(1,2,3,4,5)
if 2 in var1:
    print("present")
else:
    print("absent")

#Q11 Write a Python program to convert a list to a tuple.
list1=[1,2,3,4,5]
var1=tuple(list1)
print(var1)

#Q12 Write a Python program to remove an item from a tuple.
var1=(1,2,3,4,5)
list1=list(var1)
list2=list1.remove(3)
var1=tuple(list1)
print(var1)

#Q13 Write a Python program to slice a tuple
var1=(1,2,3,4)
print(var1[0:2]+var1[-1:])

#Q14 Write a Python program to find the index of an item of a tuple.
var1=(1,2,3,4)
var1.index(3)

#Q15 Write a Python program to find the length of a tuple.
var1=(1,2,3,4)
print(len(var1))

var1=("a","b","c","d")
print(tuple(reversed(var1)))