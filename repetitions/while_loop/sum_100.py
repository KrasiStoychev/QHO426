#Loops can be useful in performing calculations where these involve repetitive steps.  For example, calculating a total by summing up a large set of numbers involves repeatedly adding a number to the current total.  In such situations, a loop provides a more efficient alternative that helps reduce the amount of code that would otherwise be needed.

# Display start message
print("Calculating the sum of the first 100 numbers...")

# Declare a control variable
number = 1

# Calculate sum of first 100 numbers
total = 0

while (number <= 100):
    total = total + number
    number = number + 1

# Display result
print("...Done! The answer is", total)
