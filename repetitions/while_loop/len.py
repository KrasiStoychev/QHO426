#There are many useful built-in functions that we can use to carry out common tasks.  We have encountered some of these already (i.e. print(), input(), int(), str(), float(), etc.).  Another useful built-in function is the len() function.  This function will return the number of items in an object.  If the object is a string then this function will return the number of characters in the string.  For example, len( "Beep") will return 4 as there are 4 characters in the string "Beep".

# Ask user for phrase
print("Please enter a phrase?")
phrase = input()

# Declare a control variable
bops = 0

# Display Bops
print()

while (bops < len(phrase)):
    print("Bop ", end="")
    bops = bops + 1
