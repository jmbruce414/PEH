#!/bin/python3
import sys #system functions and params
from datetime import datetime as dt #import with alias (datetime is now dt in code)

print(dt.now())

my_name="Heath"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence"
print(sentence[:4])

print(sentence.split()) # split by space delimiter

sentence_split=sentence.split()
sentence_join= ' '.join(sentence_split) #join delimited sentence on space character
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space = "                     hello                "
print(too_much_space.strip())

print("A" in "Apple")
print("a" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower())

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

print('\n')
#Dictionaries - key/value pairs {}
drinks = {"White Russian": 7, "Old Fashion": 10, "Lemon Drop": 8}
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teedy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees['Legal'] = ["Mr.  Frond"] # add new key:pair value
print(employees)
employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)

print(drinks.get("White Russian"))
