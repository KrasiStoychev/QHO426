#We previously learnt how we can incorporate decisions into our code.  There may be occasions where we need to have nested decisions, that is, decisions inside decisions.  This need arises in situations where the decision to be made depends on the outcome of a previous decision.


# ask user what to do
#print("What should I do (play/study)?")
#activity = input()
    
# decide if beep should play or study
#if (activity == "play"):

    # ask user what to play with
    #print("What should I play with (toy/friend)?")
    #play_with = input()
    
    # decide if beep should play with toys or friend
    #if (play_with == "toy"):
        #print("I will play with my toys!")
    #else:
        #print("I will play with my friend!")
#else:
    #print("I will study")

#You may notice that in the above example that the second if statement is indented so that it is nested within the first if statement.  This means that the second if statement will only be evaluated if the condition for the first if statement is true, that is, the user enters "play".

#CLass

# Ask user for book details
print("What type of cover does this book have?")
cover_type = input()

# Display appropriate message
if (cover_type == "soft"):
    print("Is the book perfect-bound?")
    perfect_bound = input()

    if (perfect_bound == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books") 
else:
    print("Books with hard covers can be more expensive!")
 



