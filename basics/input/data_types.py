print("what is your mane human?")
name = input()

print("how old are you?")
age = int(input())

print("How tall are you (in meters)")
height = float(input())

print("How much do you weight (in KG)")
weight = float(input())
bmi = weight/(height**2)
print(name, "you are",age,"years old and your BMI is",bmi)
print(f"{name} you are {age} years old and your BMI is {bmi} ")