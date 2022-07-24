#We wish to create a program to help Beep and Bop cross the bridge.

#The program should start by defining a function that has the name cross_bridge and which takes 1 parameter representing the distance of the bridge crossed (in steps).
#The function should do the following:
    #Display the message "Crossed step" for each step crossed
    #If the distance is more than 5 then the message "The bridge is collapsing!" should be displayed.
    #Otherwise the message "we must keep going!" should be displayed.
#, the program should contain the following calls to your cross_bridge function:

def crossed_bridge(steps):
    # Display each step 
    for step in range(steps):
        print("Crossed step.") 

    # Display message
    if (steps > 5):
        print("The bridge is collapsing!")
    else: 
        print("We must keep going!")
