#Q1
def add_num(a,b):#function for multiplication
    multiply=a*b;
    return multiply; #return value
num1=int(input("input the number one: "))#input from user for num1
num2=int(input("input the number one: "))#input from user for num2
print("The product is",add_num(num1,num2))#call te function

#Q2
def sum_num(a,b):#function for add
    add=a+b;
    return add; #return value
num1=int(input("input the number one: "))#input from user for num1
num2=int(input("input the number one: "))#input from user for num2
print("The Sum is",sum_num(num1,num2))#call te function

#Q3
def factorial(num):#function definition
    fact=1
    for i in range(1, num+1):#for loop for finding factorial
        fact=fact*i
    return fact    #return factorial
number=int(input("Please enter any number to find factorial: "))
result=factorial(number)#function call and assign the value to variable result
print("The factorial of %d = %d"%(number,result))

#Q4
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i)

 # Q5
      def swap_numbers(a, b):
           temp = a
           a = b
           b = temp

           print("After Swapping two Number: num1 = {0} and num2 = {1}".format(a, b))


       num1 = float(input(" Please Enter the First Value : "))
       num2 = float(input(" Please Enter the Second Value : "))

       print("Before Swapping two Number: num1 = {0} and num2 = {1}".format(num1, num2))
       swap_numbers(num1, num2)


#Q6
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = int(input(" Please Enter the First Number : "))
num2 = int(input(" Please Enter the Second Number : "))

print("The H.C.F. is", compute_hcf(num1, num2))


#Q7
c = (input(" Please Enter the Alphabet : "))
print("The ASCII value of '" + c + "' is", ord(c))


#Q9
import datetime
from datetime import date
print ("Present date is : ",end="")
print (date.today())


#Q10
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return;

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")


# Q11
# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


# Q12
# Python program to demonstrate
# default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)


# Q13
# Python program to illustrate
# *args for variable number of arguments
def myFun(*argv):
    for arg in argv:
        print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')