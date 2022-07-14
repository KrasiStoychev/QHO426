seq = input("Please enter a sequense ")
marker = input("Please enter marker :")
pos1 = -1
pos2 = -1 

for i in range(0, len(seq)):
  if (seq[i] == marker):
    if pos1 == -1:
       pos1 == i
    else:
      pos2 = i

print(f"The distance between the markers is {pos2 - pos1}")