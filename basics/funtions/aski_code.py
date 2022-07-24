#let the user know that program have started 
print("Program Started!")
#take user input and store it 
print("Please enter a standard character:")
character = input()
#print charecters
if (len(character) == 1):
    print("The ASCII code for {} is {}".format(character, ord(character)))
else:
    print("A single character was expected.")

#end program
print("Program Ended!")  