print("program started")
print("Please enter asci code")
x = abs(int(input()))
if x in range(32, 127):
  print(f"The character represented by the ascii code {x} is {chr(x)} ")
print("The program ended!")