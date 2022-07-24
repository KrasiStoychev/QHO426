
#t is often useful to sort a set.  We can do this by using Python's built-in function sorted:

#sorted(web_browsers)

#To sort in reverse, we can use the parameter reverse with the boolean value True:

#sorted(web_browsers, reverse=True)

#[Tasks]

#We wish to create a variation of our previous program to help Beep and Bop record their #observations.

#The program should consist of the following three functions:

#The first function should be named observed and should have no parameters.
#The function should create a list named observations.
#The function should populate the list with 5 values read in from the user.  There should be #some duplicate values.
#Finally, the function should return the list named observations.
#The second function should be named remove_observations and should take 1 parameter.
#The function should ask the user if they wish to remove observations.
#While the user wishes to remove observations, the function should
   # Prompt the user to enter a string representing the observation (e.g. "Skyscraper") to #be removed
    #The observation should then be removed from the list
#The third function should be named run and should have no parameters.
#The function should call the first function and store the returned list in a local variable.
#The function should then call the second function with the previously retrieved list.
#Finally, the function should display a sorted set of the observations and how many times #each observation has been made.
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

#Do you wish to remove an observation (yes/no)?
#yes

#What observation do you wish to remove?
#Skyscraper
#Done!

#Do you wish to remove an observation (yes/no)?
#no

#Observations:
#Neon Sign observed 3 times
#Skyscraper observed 1 times
#Start by creating a new python file sorted_set.py and store the file in the following #location:
#data/sets/sorted_list.py







def observed():
  observations = []

  for count in range(5):
    print("Please enter an observation:")
    observations.append(input())

  return observations


def remove_observations(observations):
  is_running = True

  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    response = input()

    if (response == "yes"):
      print("Please enter the observation you wish to remove")
      observation = input()
      observations.remove(observation)
    else:
      is_running = False

def run():
  observations = observed()
  remove_observations(observations)

  # populate set
  observations_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observations_set.add(data)

  # display set
  for data in sorted(observations_set):
    print(f"{data[0]} observed {data[1]} times.")

run()