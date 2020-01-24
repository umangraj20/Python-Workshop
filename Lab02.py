#Ques.01
num=int(input("Enter a number:"))
if (num % 2) == 0:
    print("number is even")
else:
        print("number is odd")

#Ques.02

year = 2000
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#Ques.3

c=input("please enter a character:")
if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u" or c=="A" or c=="E" or c=="I" or c=="O" or c=="U"):
    print("the given character",c,"is a vowel")
else:
    print("the given character",c,"is a consonant")

#Ques.4

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number: "))
if (num1 < num2):
    print("{} is smallest".format(num1))
elif (num2 < num1):
    print("{} is smallest".format(num2))
else:
    print("{} and {} are equal".format(num1, num2))

#Ques.5

def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


num = 8
print("Factorial of", num, "is",
      factorial(num))

#Ques.6

size= 4
a=(2*size)-2

for i in range (0,size):
    for j in range (0,a):
        print(end=" ")
    a=a-1
    for j in range (0,i+1):
        print("*",end=' ')
    print(" ")

#Ques.7

def PrintNumber(N, Original, K, flag):
    print(N, end=" ")

    if (N <= 0):
        if (flag == 0):
            flag = 1
        else:
            flag = 0

    if (N == Original and (not (flag))):
        return

    if (flag == True):
        PrintNumber(N - K, Original, K, flag)
        return

    if (not (flag)):
        PrintNumber(N + K, Original, K, flag);
        return


N = 20
K = 6
PrintNumber(N, N, K, True)

#Ques.8

num = 407
num = int(input("Enter a number: "))
if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")
else:

    print(num, "is not a prime number")

#Ques.9

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")