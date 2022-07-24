#The step value of the range function can be particularly useful when we wish to generate various number sequences. For example,
#range(1, 10, 1) produces the following list of numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9 (natural numbers)
#range(1, 10, 2) produces the following list of numbers: 1, 3, 5, 7, 9 (odd numbers)
#range(0, 10, 2) produces the following list of numbers: 0, 2, 4, 6, 8 (even numbers)




# Ask user for brightness level
print("What level of brightness is required?")
brightness_desired = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 2):
    print("Beep's brightness level:", "*" * brightness)
    print("Bop's brightness level:", "*" * brightness)
    
print("Adjustments complete!")
  