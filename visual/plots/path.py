import matplotlib.pyplot as plt

def coordinate():
    x = int(input("Please Enter value for : x "))
    y = int(input("Please enter value for : y "))
    return x,y

def path():
    print("Retriving path...")
    x_values = []
    y_values = []
    for i in range(4):
       data = coordinate()
       x_values.append(data[0])
       y_values.append(data[1])
    return x_values,y_values

  
def run():
    values = path()
    plt.plot(values[0],values[1], "ro--")
    plt.show()

run()
    
