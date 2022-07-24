print("Please select how many colums? : ")
colums = int(input)

print("Please enter enter how many rows")
rows = int(input)

for row in range(0,rows,1):
   for i in range(0,colums,1):
     print("O:)", end="")
print()