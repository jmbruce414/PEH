#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war."
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #titlecase

print(len(quote))

name ="Heath" #string
age = 30 #int int(30)
gpa = 3.7 #float float(3.7)print

print(int(age))
print(int(30.1))

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1

age+=1
print(str(age) + "\n")

#functions
print("Here is an example function: ")

def who_am_i(): #this is a function
	name = "Heath"
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")

who_am_i()

#adding parameters
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#multiple params
def add(x,y):
	print(x+y)

add(7,8)

def multiply(x,y):
	return x*y

print(multiply(7,7))

def square_root(x):
	print(x ** .5)

square_root(64)

def nl():
	print('\n')

nl()

#boolean expressions
print("Boolean expressions:")

bool1=True
bool2=3*3 == 9
bool3=False
bool4= 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

nl()
#relational and boolean operatiors
greater_than = 7>5
less_than= 5<7
greater_than_equal_to= 7>=5
less_than_equal_to= 7<=7

test_and= (7>5) and (5<7) #True
test_and2= (7>5) and (5>7) #false
test_or= (7>5) or (5<7) #true
test_or2= (7>5) or (5>7) #true

test_not = not True #False

nl()
#conditional statements
def drink(money):
	if money >=2:
		return "You've got yourself a drink"
	else:
		return "No drink for you"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age>=21) and (money>=5):
		return "We're getting a drink"
	elif (age>=21) and (money<5):
		return "Come back with more money"
	elif (age<21) and (money>=5):
		return "Nice, try kid"
	else:
		return "Youre too poor and too young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))
print(alcohol(20,5))

nl()
#lists - have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[0])
print(movies[1])#second element
print(movies[1:4])#elements 1-3, exclusive 4
print(movies[0:])#first element through last
print(movies[:2])#up to element 2
print(movies[-1]) #last item

print(len(movies))
movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(0)
print(movies)

nl()
#tuples - do not change, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
#looping

#for loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print(x)

#while loops - execute as long as conditon is true

i=1

while i<10:
	print( i)
	i+=1
