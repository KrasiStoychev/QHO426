#A list is a data structure that stores elements in the order in which they are inserted.In #python, we can create a list using square brackets [ ]. For example, we can create an empty #list and assign this to a variable named fruits as follows:

#fruits = []

#We can also initialise our list with some items by providing these between the square #brackets:

#fruits = ["apple", "banana", "cherry"]

#We can add an item to the end of an existing list by using the append method (a function) of #list:
#fruits.append("dragon fruit")

#Similarly, we can remove an existing item from our list using the remove method (a function) #of list which will remove the first occurrence of the item:
#fruits.remove("dragon fruit")


def movements():
  path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  return path

def run():
  print("Moving...")
  path = movements()
  print(f"{path[0]} for {path[1]} steps")
  print(f"{path[2]} for {path[3]} steps")
  print(f"{path[4]} for {path[5]} steps")
  print(f"{path[6]} for {path[7]} steps")

run()



#With index loop:

#def movements():
  #path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  #return path

#def run():
  #print("Moving...")
  #path = movements()
  #for index in range(0, len(path), 2):
    #print(f"{path[index]} for {path[index+1]} steps")

#run()