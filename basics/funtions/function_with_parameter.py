#A parameter (also known as a formal argument) is an input to a function. Parameters allow us to pass information into functions.  Parameters are set when the function is called with suitable values (also known as actual arguments).

#The diagram below shows how a function can be invoked in Python:
#We say that Python functions are invoked through call-by-object-reference - values are bound to objects and references to the objects are passed when a function is invoked.


# The function with a single parameter named 'plan'
def escape_by(plan):
    # Determine which message to display
    if (plan == "jumping over"):
        print("We cannot escape that way! The boulder is too big!")
    elif (plan == "running around"):
        print("We cannot escape that way! The boulder is moving too fast!")
    elif (plan == "going deeper"):
        print("That might just work! Let's go deeper!")
    else:
        print("Not sure about that plan!")

# Calls to the function
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper") 