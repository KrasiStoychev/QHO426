#We previously learnt how we could use python’s built-in function print to display characters on the screen. It is often useful for a program to also be able to receive user input.  Python allows us to read user input using the built-in function input. We can assign the result of this built-in function to a variable. A variable is simply a memory location that is reserved by your program for storing a value. By assigning the value returned by the input function to a variable we make it available for use later in the code.

# Ask user for name
print("What is your name human?")

# Read user's response
name = input()

# Display confirmation message
print(f"Nice to meet you human {name}")
