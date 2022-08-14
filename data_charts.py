import matplotlib.pyplot as plt
#line 
x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x, y)
plt.show()

#with dots we have to specefi the marker "o" afeeter plt.plot(x,y,"o")
import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.plot(x, y, "o")
plt.show()

#step chart
mport matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.step(x, y)
plt.show()


#bar chart
import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

plt.bar(x, y)
plt.show()

#pie chart 
import matplotlib.pyplot as plt

labels = ('A', 'B', 'C', 'D')
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels)
plt.show()

# marker styles can be specified using single characters
# these include o for circles, s for squares, ^ for triangle up, v for triangle down

plt.plot(x, y, 'o')   # will display circle markers
plt.plot(x, y, 's')   # will display square markers

# similarly, we can control the line styles
# these include - for solid lines, -- for dashed lines, -. for dash-dot lines, : for dotted lines

plt.plot(x, y, 'o-')  # will display circle markers with a solid line
plt.plot(x, y, 'o--') # will display circle markers with a dashed line
plt.plot(x, y, 'o:')  # will display circle markers with a dotted line

# colors can be specified using single characters where r is red, b is blue, g is green, etc.
# supported colours include red, blue, green, cyan, magenta, yellow, black and white.

plt.plot(x, y, 'yo')   # will display yellow markers
plt.plot(x, y, 'ro--') # will display a red dashed line