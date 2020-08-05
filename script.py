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
