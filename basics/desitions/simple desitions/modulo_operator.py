#We have come across a number of common operators including the arithmetic operators (+, -, /, *), assignment operators (=, +=, -=) and comparison operators (==, !=). There are many more operators which are available to us and you can learn about these by clicking here.

#One particularly useful arithmetic operator is known as the modulo operator which is represented by a % character. The modulo operator returns the remainder of dividing one operand by another. For example, 10 % 3 divides 10 by 3 and returns a remainder of 1. You can learn more about the modulo operator by clicking on this link.


# Ask user for a number 
print("Please enter a whole number.")
number = int(input()) 

# Display relevant message
if (number % 2 == 0):
    print(f"\nThe number {number} is an even number.")
else:
    print(f"\nThe number {number} is an odd number.")
