#We have learnt how we can devise decision making structures by nesting decisions in our code.  However, having a heavily nested structure quickly increases the complexity of our program and can make it more difficult to understand the code.  To improve the readability of the code and provide us with greater flexibility we can implement decisions with multiple conditions using logical (and, or and not) operators.
#The logical operators work by evaluating expressions from the left to the right. 
#In the case of the and operator the expressions on both sides of the operator must evaluate to True. 
#In the case of the or operator an expression on other side of the operator must evaluate to #True.

#In the case of the not operator only one of the expressions must evaluate to True.

#We can summarise these operators visually as follows:
# Ask user for the type of adventure 
print("What type of adventure should I have?")
adventure_type = input() 

# Determine what message to display
if ( (adventure_type == "scary") or (adventure_type == "short") ):
    print("\nEntering the dark forest!")
elif ( (adventure_type == "safe") or (adventure_type == "long") ):
    print("\nTaking the safe route!")
else:
    print("\nNot sure which route to take.")