#
# Title:    Chapter 1
# Purpose:  Code and notes for chapter 1 in Automating Python
# Author:   Billy Caughey
# Date:     2020.08.15 - Initial Build
#

##### Entering Expressions into the Interaction Shell #####

# Expression
2 + 2

# Exponetial
2 ** 3

# Modulus/reminder
22 % 8

# Division
22 / 8

# Multiplication
3 * 5

# Subtraction
5 - 2

# Addition
2 + 2

# Order of Operations = Precedence

2 + 3 * 6
(2 + 3) * 6

2 ** 8

##### The Integer, Floating-Point, and String Data Types #####

# the most common data types are: integers, floats, and strings

x = 'Hello, world!'
print(x)

y = 1
print(y)

z = 2.4
print(z)

##### String Concatenate and Replication #####

# when strings are considered, '+' is the Concatenate function

'Alice' + 'Bob'

'Alice' * 5 # This will return Alice, repeated 5 immediate times

##### Storing Values in Variables #####

spam = 40
spam

eggs = 2
eggs

spam = spam + 2
spam

spam = 'Hello'
spam

spam = 'Goodbye'
spam

# A good variable describes the data it contains

##### Your First Program #####

print('Hello, world!')
print('What is your name?')
myName = input()
print(len(myName))

print('What is your age?')
myAge = input()
print("You will be " + str(int(myAge)) + ' in a year')
