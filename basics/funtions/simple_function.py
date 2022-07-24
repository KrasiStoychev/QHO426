#In Python, functions can be defined by using the keyword def, a function name and zero or more parameters (inputs to the function). As a simple example, consider the following program to display a greeting:

#print("Please enter your name")
#name = input()
#print("Hello", name)
	
#We can turn this into a function as follows:

# The function
#def greet_user():
  #print("Please enter your name")
  #name = input()
  #print("Hello", name)
	

#In the above code, the keyword def has been used to indicate that we are defining a function. The function has been named greet_user and has been defined as taking no parameters as indicated by the empty brackets that follow the name of the function. Notice that the statements of code have been indented to indicate that they are part of the function.

#Executing the above program will result in no output being displayed. That is because once a function has been defined it must be called in order to be used. To call a function we simply call it by its name and supply any arguments that required by the function. Thus, to add a call the previous function we would do the following:

# The function
#def greet_user():
  #print("Please enter your name")
  #name = input()
  #print("Hello", name)

# Call to function
#greet_user()

#Running the above program will now result in the greeting being displayed. We can display the greeting multiple times by simply making multiple calls to the function as shown in the following example:

# The function
#def greet_user():
  #print("Please enter your name")
  #name = input()
  #print("Hello", name)

# Calls to the function
#greet_user()
#greet_user()
#greet_user()

#In class

# The function
def listen():

    # Ask user for the sound 
    print("What sound did I hear?")
    sound = input() 

    # Display message
    print("\nThat was a loud", sound)


# Call to function
listen()
