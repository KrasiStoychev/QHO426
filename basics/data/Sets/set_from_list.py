#We can also initialise a set with other immutable data structures such as a tuple

#web_browser_usage = {("Chrome", 10), ("Firefox", 9), ("Edge", 3)}
#As a set cannot contain duplicate elements, any duplicate tuples will be removed to leave us #with a set containing unique tuples.  For example, if we added the tuple ("Edge", 3) then #this will be ignored as it is a duplicate.

#We can add an element to a set by using the method (a function) add of set which will add an #element using hashing.

#web_browser_usage.add(("Opera", 1))

#We can remove an existing element from our set using the method (a function) remove:
#web_browser_usage.remove(("Edge", 3))


#[Tasks]

#We wish to create a program to help Beep and Bop record how many of each type of item they saw (e.g. 2 skyscrapers, 5 neon signs, etc.).

#The program should consist of the following two functions:
#The first function should be named observed and should have no parameters.
#The function should create a list named observations.
#The function should populate the list with 7 values read in from the user.  There should be #some duplicate values.
#Finally, the function should return the list named observations.
#The second function should be named run and should have no parameters.
#The function should start by displaying the message "Counting observations...".
#The function should then call the first function and store the returned list in a local variable.
#The function should then create a set that contains a tuple for each unique value in the list along with a count for how many times that value appeared in the list e.g. ("Skyscraper", 2)
#Finally, the function should display the content of the set.

#An example run of such a program is shown below:

#Counting observations...
#Please enter an observation:
#Skyscraper
#Please enter an observation:
#Skyscraper
#Please enter an observation:
#Neon Sign
#Please enter an observation:
#Neon Sign
#Please enter an observation:
#Neon Sign
#Please enter an observation:
#Neon Sign
#Please enter an observation:
#Neon Sign

#Skyscraper observed 2 times.
#Neon Sign observed 5 times.

#Start by creating a new python file set_from_list.py and store the file in the following location:
#data/sets/set_from_list.py






def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation:")
    observations.append(input())

  return observations

def run():
  print("Counting observations...")
  observations = observed()

  # populate set
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  # display set
  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times.")

run()