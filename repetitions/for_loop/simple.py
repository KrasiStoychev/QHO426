#We previously learnt how loops can be used to perform repetitive tasks.  Thus far we have come across one type of loop known as the while loop.  This type of loop is useful when we wish to repeat a block of code as long as a specific condition remains True.  Most programming languages provide multiple loop structures each suited to a different set of tasks.  One popular alternative is to use a for loop.  This type of loop is particularly suited to scenarios where we wish to repeat a block of code for a specific number of iterations.
#Consider the scenario where we wish to create a program to display 100 ASCII faces.  In this case, the number of iterations is known (100) and hence a for loop is appropriate for use in this scenario.
#The code for drawing 100 faces using a for loop is as follows:
#for count in range(100):

#[Explanation]
#The for loop may look a little different to the while loop but it essentially performs the same function.
#for count in range(0, 100, 1):
    #print("#########")
    #print("#       #")
    #print("# O   O #")
    #print("|   V   |")
    #print("|  ---  |")
    #print("|_______|")

#In the code above count is a variable which is local to the for loop.  This means that it only exists inside of the loop and for the lifetime of the loop.  The variable count cannot be referenced from outside of the loop. We call this the scope of the variable.



#for count in range(0, 100, 1):
   # print("#########")
    #print("#       #")
    #print("# O   O #")
    #print("|   V   |")
    #print("|  ---  |")
    #print("|_______|")

#The code above also contains range which is a function that creates a sequence of numbers ranging from 0 to 99 (i.e. up to but not including 100). The range function has three parameters (variables of the function that can receive values).  These represent the start, stop and step of the sequence. We can supply arguments (values for each parameter) to control the behaviour of the range function and subsequently our loop. For example, the following code is equivalent to the previous example:
#In the above example, the starting value of the sequence is 0, the stopping value is 100 and the step (difference between each number in the sequence) is 1. We can learn more about the range function here.

#In terms of functionality for loops and while loops are usually interchangeable.  That is, what can be achieved using one loop can be achieved using the other. The key difference between the two loops is their semantic meaning. A for loop is used for a fixed number of steps i.e. it is known how many repetitions will occur whilst a while loop is used when it is not known how many repetitions will occur.

#We can learn more about loops here.

#iN CLASS ACTIVITY

# Ask user for number of mountains

print("How many mountains should I display?")
mountains = int(input())

# Display mountains
print("\nDisplaying...")

for mountain in range(mountains):
 print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)