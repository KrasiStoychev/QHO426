# define the first function and pass the first parametar "steps" then use a 'for' loop to print each step of the ladder based on the variable value that we are gonna take from the user in the secound function
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
     