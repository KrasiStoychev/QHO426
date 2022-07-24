#Let us now consider an example where we wish to display the greeting "Hello" and the user's name in an ASCII box. We could do the following:

#def display_box(name):
  #message = "* Hello {} *".format(name)
  #print("*" * (len(message))
  #print(message)
  #print("*" * (len(message))
  
#def greet_user():
  #print("Please enter your name")
  #name = input()
  #display_box(name)
  
#greet_user()

#The above example contains the definition of two functions. The first function, greet_user, is called first and this function in turn then calls the display_box function.  The display_box function takes a single parameter representing the name and so when calling this function we supply an argument with the value entered by the user. When the display_box function completes execution, the program returns to the function call in the greet_user function and subsequently to the original function call.

#At this stage you may find it useful to use the Python Visualiser tool to help you understand functions and other aspects of your python program.




# define the first function and pass the first parametar "steps" then use a 'for' loop to print each step of the ladder based on the variable value that we are gonna take from the user 
#in the secound function


def display_ladder(steps):
    for step in range(steps):
         print("| |")
         print("***")
#Take user input and store it in a varable'steps'that is passed to the finction that prints the steps, then call the function that print the ladder steps with assing value of 'steps'
def create_ladder():
     print("Please enter how many steps? :")
     steps = int(input())
     display_ladder(steps)

#Call the function to start the program
create_ladder()
     