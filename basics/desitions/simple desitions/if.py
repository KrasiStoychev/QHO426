#We will now learn about coding decisions. There are a number of ways of coding decisions but the most common approach is to use if statements. An if statement is a conditional statement that has a logical outcome. It checks whether a condition is true and if so, executes additional statements. You can think of it as providing an alternative path through the code when a certain condition is satisfied.


# Ask user for the type of book 
print("What type of book is this?")
book_type = input() 

# Determine if the book is an adventure book
if (book_type == "adventure"):
    print("I like adventure books!")

# Display message
print("Finished reading book")