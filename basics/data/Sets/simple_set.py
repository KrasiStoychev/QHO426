#A set is a fundamental concept in mathematics and is the basis of a dedicated branch of study known as Set Theory.
#In Python, a set is an implementation of its equivalent mathematical concept, that is, a set is a collection of distinct objects which are known as elements or members of the set.  A set does not contain duplicates and may be defined by a membership rule or by listing its members.
#A set is an unordered data structure which cannot be indexed and contains immutable objects #although the set itself may be mutable(Python also has immutable sets known as frozen sets).
#Internally, the set utilises hashing to determine how to store and access an element.  This #involves creating a hash value for an element using a hashing algorithm and storing the #element based on its hash value. 

#Hashing Algorithm

#The Python implementation for a set supports operations derived from Set Theory including the union, intersection and difference of sets as summarised in the table below.
#Function	Description
#len(s)	The number of elements in set s (known as cardinality of s).
#x in s	Test x is a member of set s.
#x not in s	Test x is not a member of set s.
#s.add(el)	Adds the element el to the set s.
#s.discard(el)	Removes the element el from the set s if it is contained in the set s. If #not, nothing will happen.
#s.remove(el)	Removes the element el from the set s if it is contained in the set s. If not, a KeyError will occur.
#s.issubeset(t)	Test whether every element of set s is in set t.
#[Equivalent to s <= t]
#s.issuperset(t)	Test whether every element of set t is in set s.
#[Equivalent to s >= t]
#s.union(t)	Creates a new set with elements from both set s and set t.
#[Equivalent to s | t]
#s.intersection(t)	Creates a new set with elements that are common to both set s and set t.
#[Equivalent to s & t]
#s.difference(t)	Creates a new set with elements that in set s but not in set t.
#[Equivalent to s - t]
#s.symmetric_difference(t)	Creates a new set with elements in either set s or set t but not both.
#[Equivalent to s ^ t]
#s.copy()	Creates a new set with a shallow copy of set s.
#del s	Deletes the set s.



#We can create a set in python using the function set().  For example, if we wish to create a set representing web browsers then we can do this as follows:

#web_browsers = set()

#We can create and initialise our set with some elements by providing these between the curly brackets:

#web_browsers = {"Chrome", "Firefox", "Edge"}

#We wish to create a program to help Beep and Bop record what they can see in the distance.

#The program should consist of the following two functions:

#The first function should be named observed and should have no parameters.
#The function should create a set named observations.
#The function should populate the list with the following items: "Flying Car", "Sky Scraper", #"Laser" and "Dome". 
#Finally, the function should return the set observations.
#The second function should be named run and should have no parameters. 
#The function should call the first function and display the set returned by the call.

#An example run of such a program is shown below:

#{'Flying Car', 'Sky Scraper', 'Laser', 'Dome'}

#Start by creating a new python file simple_set.py and store the file in the following location:

#data/sets/simple_set.py

def observed():
  observations = {"Flying Car", "Sky Scraper", "Laser", "Dome"}
  return observations

def run():
  print(observed())

run()