#Dictionary = A changeable ,unordered collection of unique key:value pairs that allow us to acces value quickly beacouse they use hashing.

capitals = {'USA':'Washington DC',
            'India':'Deli' , 
            'China':'Beijing' ,
            'Russia':'Moscow'}

#print(capitals[Russia]) - not safe cuz if the key is missing the program crashes the solution is the use the get function


print(capitals.get('Russia'))


#With dictionary we can also print just the values with'.values() function :
print(capitals.values())

#Or we can print just the keys with .keys()  :
print(capitals.keys())

#Or we can print everything by using .items funtion : 
print(capitals.itels())

#Another way to display all items in the dictionary is with a "for loop" : 

for key,value in capitals.items():
    print(key,value)

#Future of dictionary is that is mutable and we can change it after that program already run by use the " Update methon "

capitals.update({'Geramny':'Berlin'})

#We can also update an existing Item in the dictionary lets say i want to change the the capital of USA : 
capitals.update({'USA':'Sofia'})

#Removing an item from the dictionary is made by using the pop method :
capitals.pop('china')
#and when u print the item is your dictionary china will not apear 

#In oreder to Clear all item in the dictionary use the .clear() method