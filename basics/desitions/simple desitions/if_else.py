#We can specify what statements should be executed when the condition of an if statement is evaluated to false.



# Ask user for the type of activity
print("Please enter the activity to be performed.")
activity = input() 

# Determine if the activity is calculate
if (activity == "calculate"):
    print("Performing calculations")
else:
    print("Performing activity")

# Display message
print("Activity completed.")
