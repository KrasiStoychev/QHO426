#A tuple is similar to a list in that it is an ordered data structure that uses an indexing to store and retrieve items. However, unlike a list, a tuple is an immutable data structure.  This means that once it has been created, it can not be modified.  In Python, we can create a tuple using round brackets ( ) or the function tuple( ). For example, we can create a tuple with heterogeneous data and assign it to a variable named person as follows:

#person = ("Prins", 36, "Senior Lecturer")

#As a tuple is immutable, it does not have functions to add or remove items.  However, we can perform some useful basic operations including concatenation, repetition and membership as shown in the following example where we have a tuple with some temperature data:
#temperatures = (19, 23, 21, 21, 20, 18, 22)

# Concatenate tuples (this creates a new tuple)
#all_temperatures = temperatures + (20, 21)
#print(all_temperatures)

# Repeat a tuple
#print(temperatures * 2)

# Check membership of a tuple
#print(20 in temperatures)

#Tuples also support some useful functions such as min which gets the smallest value in a tuple and max which gets the largest value in a tuple:
#print("The lowest temperature is: {}".format(min(temperatures)))
#print("The highest temperature is: {}".format(max(temperatures)))

#define the function and populate the tuple and return the smallest value from the list using'min()' - function

def likelihood():
  likelihoods = (50, 38, 27, 99, 4)
  return min(likelihoods)
#define function and print format messege using'{}' that takes smalest number from the list - 'likelihood ' cuz we used min() - function on it 
def run():
  print(f"Minimum likelihood of falling: {likelihood()}%")
#call the function to run it 
run()