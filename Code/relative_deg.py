#!/usr/bin/env python
import math
import matplotlib.pyplot as plt

def makePoint(deg, dist, x1, y1, commands):

	angle = 90 - deg

	if(deg > 90):
		angle = 360 - (deg - 90)


	if(math.cos(angle) < 0 or deg > 90):
		(x2, y2) = (x1 + dist*math.cos(angle)*-1, y1 + dist*math.sin(angle)*-1)
	else:
		(x2, y2) = (x1 + dist*math.cos(angle), y1 + dist*math.sin(angle))

	if(deg < 0 or deg > 90):
		(x2, y2) = (x2 * -1, y2 * -1)

	return (x2, y2)


# Main Script -------------------

points = [(0, 0)]
commands = [" "]


points.append(makePoint(140, 15, 0, 0, commands))
plt.plot(*zip(*points), color='red', marker='o')
plt.grid()
plt.show()

