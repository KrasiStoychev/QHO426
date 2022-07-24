##A module is a file that contains Python code such as variables, functions and even complete runnable solutions similar to those we have created in the previous activities for this module.  We can group related code into a module to make it easier to understand and use the code.  We can create multiple modules which can work together (with one module importing another) to provide suitably structured solutions.  Modules can be shared and utilised so as to allow developers to create solutions efficiently.
#Python includes a number of modules as part of its standard library.  We will learn about and utilise some of these. 
#Let us consider the example where we wish to generate pseudo-random numbers. Python provides a module known as random which implement pseudo-random number generators.  We can use the functions in this module to quickly generate a random number.  We can start by importing the module as follows:
#import random

#The above code will import all the variables and functions in the random module and make it available to our program.  It is often convenient to rename modules with abbreviated names in code.  This is particularly useful where we have long module names or we are referring to sub-modules.  For example, we can use the variable rnd to refer to the imported module:
#import random as rnd

#Now that the module has been imported, we can use the functions contained in the imported module.  For example, we can call the function randrange which generates a random number in a given range.

#import random as rnd

#print(rnd.randrange(1, 10, 1))

#It is also possible to only load parts (a variable, function, etc.) rather than an entire module.  We can do this using the keyword from.

#from random import randrange

#print(randrange(1, 10, 1))




import random

print("Please enter the minimum value:")
min_value = int(input())

print("Please enter the maximum value:")
max_value = int(input())

random_number = random.randrange(min_value, max_value)

print("I am thinking of a number between {} and {}.".format(min_value, max_value))
print("Can you guess what it is?")

guess = 0

while(guess != random_number):
  print("Please enter a number:")
  guess = int(input())

  if (guess == random_number):
    print("Congratulations!")
    break
  elif (guess < random_number):
    print("Guess higher")
  else:
    print("Guess lower")
  
print("Game over!")