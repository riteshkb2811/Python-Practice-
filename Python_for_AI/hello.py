# Imports
import math

import array

from functools import reduce

import json

# Printing, variables, and basic values
print("Hello")
name ="Ritesh"
print (name)
age =18
can_vote=age>=18
print(can_vote)
is_age=age==18
has_license=False
can_drive=age>=18 and has_license
print(can_drive)

# String concatenation
str="Ritesh"
str2="Hi,My name is"
print(str2+" "+str)

# Boolean logic and if statements
overspeed =True
drunk=False
if overspeed or drunk:
    print("fucked up")

# Nested for loops and pattern printing
for i in range(0,6):
    for j in range(0,i):
          print("*",end="")
    print("")

# Lists, dictionaries, tuples, and sets
lst=[10,20,"Ritesh","Yash",89]
print(lst)

dict={1:"Ritesh",2:"Om",3:"Yash"}
print(dict)
dict[4]="om"
print(dict)
tup=(10,20,30,40)
print(tup)
print(tup)
empty={10,20,20,30,40}
print(empty)
empty=set(["Ritesh","yash","Om","Om","Aditya"])
print(empty)

# Recursive function
def rsk(i,n):
     if i>n:
          return
     rsk(i+1,n)
     print(i)
     
rsk(0,5)

# Default and keyword function arguments
def name(firstname="Ritesh",lastname=""):
     print(f"My name is {firstname} {lastname}")

name(lastname="Kamble")

# Function parameters and simple interest calculation
def interest(p,n,r):
    print("Simple interest is",p*n*r/100)

interest(100,2,3)


# Local variables and the id() function
a=10
def add():
     a=20
     b=30
     return a+b
add()
print(id(a))


# Complex numbers and type checking
c=8+9j
print(type(c))

# Defining and calling a function
def add1(a,b):
     c=a+b
     return c

d=add1(10,20)

# Functions from the math module
print(math.sqrt(4))
print(math.pow(3,2))
print(math.fabs(10.7))

i=10
o=20
i,o=o,i
print(i)
print(o)

# a=int(input("Enter the name"))
# print(a)
# Nested while loops and pattern printing
i=0
while i<=5:
 j=0
 while j<=i:
      print("*", end="  ")
      j+=1 
 print("")
 i+=1

# Typed arrays and iteration with continue
arr1 =array.array('f',[1.0,2.3,3.6,4.2,5.8,-0.6])
print(type(arr1))


for i in arr1:
  if i<0:
     continue
  print(i)
arr1.append(90)
print(id(arr1))


# Array type codes and copying values with a generator
arr2=array.array('i',[10,20,30,40,50,60,70,80])
arr3=array.array(arr2.typecode,(n for n in arr2))
print(arr2)
print(arr3)



# Variable-length positional arguments (*args)
def ns(num1,*num2):
    sum =num1
    for i in num2:
        sum+=i;
    print(sum)
ns(10,20,30,40,50)



# Global and local variables
r=10;
def fn():
    globals()['r']=20
    s=20
    print(s)
fn()
print(r)



# Recursive factorial function and user input
def func(n):
    if n == 1 or n == 0:
        return 1
    return n * func(n - 1)
print("Enter a number")
n=int(input())
print("factorial of",n,"is",func(n))



# Functions as arguments (higher-order functions)
def square(num):
   for i in num:
           print(i*i)
def cube(num): 
    for i in num:
        print(i*i*i)
def calculate(num,operate):
    return operate(num)
nums=[2,3,4]
res=calculate(nums,square)



# Lambda function
ns=lambda num:num*num
print(ns(10))


# Filtering a list with a lambda predicate
nums=[9,7,6,7,4,9,54,43,67,13]
is_even=lambda n :n % 2==0
even=list(filter(is_even,nums))
print(even)
grt=list(filter(lambda n:n>50,nums))
print(grt)

# Mapping a list with a lambda function
double=list(map(lambda n:n*2,nums))
print(double)

# Reducing a list with a lambda function
reduced=reduce(lambda a,b:a+b,nums)
print(reduced)

# Reducing a list with a lambda function to sum cubes
reduced1 = reduce(lambda total, n: total + n**3, nums, 0)
print(reduced1) 


def xyz():
    print("Hello")
    def abc():
        print("Hi")
    return abc
stq=xyz()
stq()

def greet (name):
    def message():
        return f"Hello, {name}!"
    return message

nmn=greet("Alice")
print(nmn())

# Decorators and function wrapping
def greater_num(func):
    def inner(a,b):
        if a<b:
            a,b=b,a    
        return func(a,b)
    return inner

@greater_num
def add(a,b):
    return a+b

@greater_num
def sub(a,b):
    return a-b

print(add(10,20))
print(sub(20,10))


# Decorators and logging 
def logger(func):
    def inner():
        print("hello")
        return func()
    return inner

@logger
def greet():
    print("Welcome to Python")

# Main execution block
if __name__ == "__main__":  
 print(greet())
 print(__name__)

#Generators and yielding values
def my_generator():
    yield 1
    yield 2
    yield 3

my_gen = my_generator()
for value in my_gen:
    print(value)

#JSON
x='{"name":"Ritesh","age":18,"city":"Pune"}'
y=json.loads(x)
print(y["name"])
print(y["age"])
print(y["city"])

z=json.dumps(y)
print(z)