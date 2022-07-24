#So far we have focused on one particular type of data, that is, strings. These represent sequences of text. However, there are many other data types that are available to us for use in our program. The most common of these include...

#...strings. These are sequences of text. In python, we can cast a variable to a string data type using the str() function.

#...integers. These are whole numbers that can be positive or negative. In python, we can cast a variable to an integer data type using the int() function. For example, if we wish to read in a whole number from the user, we can do the following:


# Read in user data 
print("What is your name?")
name = input() 

print("What is your age?")
age = int(input())

print("What is your weight?") 
weight = float(input()) 

print("What is your height?")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(f"{name} your bmi is {bmi}")