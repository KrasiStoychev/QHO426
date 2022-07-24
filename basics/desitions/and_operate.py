#The logical or operator is useful when we would like at least one the of boolean expressions to evaluate to True.  However there are often cases where we would like all expressions to evaluate to True.  In this case we can use the logical and operator.


# Ask user for what they saw and heard
print("What did I hear?")
hear = input() 

print("What did I see?")
see = input()

# Determine what message to display
if ( (hear == "grr") and (see == "two red eyes") ):
    print("\nThere is a scary creature. I should get out of here!")
else:
    print("\nI am a little scared but I will continue.")
