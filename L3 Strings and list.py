#Q1 WAP  to demonstrate while loop with else statement.
count = 0

while count < 3:
    print("while loop")
    count = count + 1
else:
    print("else statement")


 # Q4 WAP  to demonstrate Pass statements.
for num in [20, 11, 9, 66, 4, 89, 44]:
        if num % 2 == 0:
            pass
        else:
            print(num)

#Q5(A) Write a Python program to calculate the length of a string.

str= "hello"
count= len(str)
print(count)

#Q5(B) Write a Python program to calculate the length of a string.

count=0
for i in str:
    count= count+1
print(count)

#Q8 Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself

str1= (input("enter a string"))
print(str1)
char1= str1[0]
str2= str1.replace(char1, '$')
print(char1+ str2[1: ])

#Q9 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str1= input("enter a string:")
str2= input("enter the second string:")
print(str2[-2: ]+ str1[2:]+ " "+ str2[0:3]+ str1[0:2])

#Q10 Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged

str1= input("enter a string:")
count= len(str1)
if count>2:
    if str[-3:]=='ing':
        str1= str1[0:-3]+"ly"
    else:
        str1= str1+"ing"
print(str1)


