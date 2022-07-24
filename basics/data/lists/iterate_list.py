#A list can be iterated using a loop.  Two commonly used loops with a list are an index based for loop or a for...in loop.  The former is useful where we wish track the index position of an item in a list.  If the index is not required then the latter loop is more convenient.

#Let us say we wish to display the names of all fruits that are stored in a list named fruits.  We can do this using a for...in loop as follows:

#for fruit in fruits:
    #print(fruit)

#Now let us consider the case where we wish to also display the index position of the fruit.  We can modify our code as follows:

#for index in range(len(fruits)):
    #print("{} is at index {}.".format(fruit, index))


#in class

def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  dirs = directions()
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")

def run():
  menu()

run()