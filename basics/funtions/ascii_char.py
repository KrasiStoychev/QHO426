#it is also possible to convert an ASCII code back into a character.

#Show that program have started
print("Program Started!")
#take user input and store it 
print("Please enter an ASCII code:")
code = int(input())
#chr(i)
#Return the string representing a character whose Unicode code point is the integer i. For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. This is the inverse of ord().
#The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in base 16). ValueError will be raised if i is outside that range.
#check user input and print results
if (code >= 32 and code <= 126):
    print(f"The character represented by the ASCII value {code} is: {chr(code)}")
else:
    print("The character cannot be displayed.")
#show that the program ended
print("Program Ended!")
