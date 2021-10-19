#!/usr/bin/env python
import math
import matplotlib.pyplot as plt

def makePoint(deg, dist, points, commands):

	# angles
	alpha = deg # handles also negative DEG if point is on the Left of rover

	# alpha plus beta needs to be 90 -> regular triangle
	if (deg < 0):
		cmd = "LT"
	else:
		cmd = "RT" 

	# create point with relative grid from start point
	# startpoint and direction of rover determens grid
	# for point we use simple trigo.
	# for new point:
	if(math.sin(alpha) < 0 or cmd == "LT"):
		x = math.sin(alpha) * dist * -1
	else:
		x = math.sin(alpha) * dist

	y = math.sqrt(dist*dist + x*x)
	point = (x, y)

	points.append(point)
	commands.append(cmd)

	return points, commands


# Main Script -------------------

points = [(0, 0)]
commands = [" "]

points, commands = makePoint(34, 2, points, commands)
points, commands = makePoint(3, 24, points, commands)
points, commands = makePoint(90, 45, points, commands)
points, commands = makePoint(-13, 12, points, commands)




print(points)
print(commands)

plt.plot(*zip(*points), color='red', marker='o')
plt.grid()
plt.show()