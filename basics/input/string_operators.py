#Programming languages such as Python support a range of operators that can be used to manipulate operands (i.e. data). The behaviour of the operators is determined by the data type of data on which they operate. Basic operators such as + and * can be used on numeric data types to perform addition or multiplication, respectively. The same operators can be used with strings to concatenate or repeat strings respectively.


# Read bot data
print("Please enter number of lives")
lives = int(input())

print("Please enter energy level")
energy = int(input())

print("Please enter shield level")
shield = int(input()) 

# Display bot data
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")