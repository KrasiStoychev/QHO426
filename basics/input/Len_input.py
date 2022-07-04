name = input("Enter your name :")
#len() - funtion that returns the length of an item that u put inside
print(len(name))
if len(name) > 8:
  print("Your name is very long.Please tell me a nick name: ")
  name = input()

print(f"Wlcome {name}!")