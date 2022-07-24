#As stated previously, the range function has three parameters; start, stop and step.  We can supply arguments (values) for each of these parameters which allows us to exert greater control over our for loop.  We can for example, reverse the value supplied for the start and stop parameters and use a negative step to generate a range of numbers in descending order.


# Ask user for distance
print("How far are we from the cave?")
distance = int(input())

# Display count down
print()

for count in range(distance, 0, -1):
    print(count, "steps remaining")

print("We have reached the cave!")
  