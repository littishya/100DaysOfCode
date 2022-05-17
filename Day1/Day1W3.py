# -*- coding: utf-8 -*-
"""
Created on Sun May  8 20:46:33 2022

@author: 2063176
"""

print('Hello World')
if 5>2:
    print( "5 is greater than 2")
x = 5
y = "Hello"
print(x)
print(y)
#python variables
p = str(5)
q = float(5)
print(type(p))
print(type(q))

camelCase = "Hiiiii"
PascalCase = "Hellooo"
snake_case ="Fineee?"

a ,b, c = "mustang","corvette","koenisegg"
print(a)
print(b)
print(c)

x = y= z = "Ferrari"
print(z)

sports_cars =["poshe", "lamborgini","nissan", "ford mustang"]
print(sports_cars)

x =2
y = 4
print(x + y)

"""
9:7 pm - tired
stoped
"""
#global variables
#inside function
x = "awesome"
def myfun():
    print("Python is "+x)
myfun()
#outside function
x = "awesome"
def myfun():
    print("Python is "+x)
myfun()
print("Python is "+x)
#Create a variable inside a function, with the same name as the global variable
x = "awesome"
def myfun():
    x= "Fantastic"
    print("Python is "+x)
myfun()
print("Python is "+x)
#global keyword, the variable belongs to the global scope:
def myfunc():
    global x
    x = "Fantastic"
myfunc()
print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x ="Teddy"
def myfun1():
    global x
    x = "Ted"
myfunc()
print("Python is "+x)

#PYTHON DATA TYPES
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#str
x = "Hello World!"
#int
x = 20
#float
x = float(20.5)
#complex 
x = 1j
#list
x = ["Ferrari","Mustang","Corvette","BMW"]
#tuple
x = ("Ford","Toyota","Honda", "BMW", "Audi","Mercedes-Benz", "Porshe")
#range
x = range(10)
#dict
x = {"car": "Lamborgini", "Price":"4 Cr"}
#set
x = {"Innova","Landrover","porsshe", }
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview

#NUMBERS
#Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1,10))

#Python casting
#Integers:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#Floats:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#Strings:
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
 #PYTHON STRINGS
print("Hello")
print('Hello')

a = "Hello"
print(a)
#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Strings are Arrays
a = "Hello, World!"
print(a[1])
#Looping Through a String
for x in "banana":
  print(x)
#string length
a = "Hello, World!"
print(len(a))
#Check String /in keyword
txt = "The ultimate goal of life is gaining wisdom"
print("goal" in txt)
#Use it in an if statement:
txt = "The ultimate goal of life is gaining wisdom"
if "goal" in txt: 
    print("Yes,'goal' is present.")    
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])
#Slice From the Start
b = "Hello, World!"
print(b[:5])
#Slice To the End
b = "Hello, World!"
print(b[2:])
#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
#Python - Modify Strings #upper case
a = "Hello, World!"
print(a.upper())
print(a.lower())
#Remove Whitespace
#Whitespace is the space before and/or after the actual text,
#and very often you want to remove this space.
#The strip() method removes any whitespace from the beginning or the end:
a = "   Hello, World!   "
print(a)
print(a.strip())
#Replace String
a = "Hello, World!"
print(a.replace("H","J"))
#Split String
#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(","))
#Python - String Concatenation #String Concatenation
a = "Hello"
b = "World"
c = a+b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a+" "+ b
print(c)    
#Python - Format - Strings #String Format
age = 36
#txt = "My name is Ted, I am "+ age
print(txt)
#Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity,itemno,price))
#index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


























