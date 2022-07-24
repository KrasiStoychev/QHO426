#Our journey thus far has led us to a stage where we can incorporate decisions in to our program. However, we have already found that we often end up repeating blocks of statements particularly when solving programs that require more sophisticated solutions. This can make our programs more difficult to manage and introduce unnecessary inefficiency. There are at least two approaches that we can take to address these issues. The first is to implement loops and the other is to implement user-defined functions. At this stage, we will focus on the former approach.

#A loop allows us to repeat a statement or a block of statements and is useful in helping us to reduce the amount of coding that is necessary to solve particular problems.  There are generally two types of loops available to us - a while loop and a for loop.  We will start by learning about while loops.
#Let us consider a simple example where we wish to count the number of iterations to a maximum of 10. We can do this in python as follows:
 #Declare a variable to count the current number of iterations
#iterations = 0

# Display ready message
#print("Starting iterations...")
 
# Display the current count    
#while (iterations < 10):

    # Update the current iteration count
    #iterations = iterations + 1

# Display completion message
#print("Completed", iterations, "!")


#A while loop is similar to an if statement in that it has a Boolean expression as a condition.  The while loop contains a block of statements inside the loop body which are repeatedly executed whilst the condition is True.  In the previous example, iterations acts as a control variable that is used to control the loop. The will continue to iterate until the condition evaluates to False, that is, the control variable iterations reaches a value of 10.
#We can visualise the previous while loop using a tool such as the Python Visualizer.

#PRINTING WITH LOOPS ON THE SAME LINE 

#Note that for the above example you may find it useful to use the end parameter for the print function.  By default, when we output a message with the print function it will write out the message and then go to a new line.  We can stay on the same line by overriding the default value for end parameter so that it is set to an empty string. 
#As an example, the first statement will output a message and stay on the same line. The subsequent print statement will output its message to the same line and after move to the next line.

 #print("the second message is", end="")
 #print("on the same line")


# Ask user for number of cables
print("How many cables should I remove?")
cables_to_remove = int(input())

# Declare a control variable
cables_removed = 0

# Remove cables
print()

while (cables_removed < cables_to_remove):
    print("Removed cable.")
    cables_removed = cables_removed + 1
