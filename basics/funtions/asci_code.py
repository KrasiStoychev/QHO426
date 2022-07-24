#unctions are reusable blocks of code that perform specific tasks. They are a common feature of many programming languages and help improve the structure. They key benefits of using functions is:

#Code Reuse: A block of code can be reused multiple times by the program or even other programs
#Abstraction: A function can be used without knowing the details of how it works.
#In Python, as well as many other languages, we generally have two categories of functions - #built-in functions and user-defined functions.

#Built-in functions are functions that are part of the standard libraries of the programming #language. Python functions such as print and input are built-in functions.
#User-defined functions are functions written to address certain requirements. They can improve code reuse and extend capabilities beyond that provided by the standard libraries.
#We have already encountered some built-in functions including print, input, format, range and those for converting data types (int, float, str).  Python provides many built-in functions for common tasks and our convenience.  A list of these can be found in the table #below:


#take user inputlet the user know the pogram have started
int("Program Started!")

#take user input and store it in a varable
print("Please enter a standard character:")
character = input()

#printing results
if (len(character) == 1):
    print("The ASCII code for {} is {}".format(character, ord(character)))
else:
    print("A single character was expected.")
  
#program ended
print("Program Ended!")