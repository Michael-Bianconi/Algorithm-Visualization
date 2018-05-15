"""Highest Number Visualization

	Perhaps the most rudimentary algorithm. Given
	a list, find and return the highest number.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def find(list):
	if len(list) == 0: return
	high, high_index = list[0], 0
	for i, x in enumerate(list):
		rects[i].set_color('blue')
		if i-1 != high_index:
			rects[i-1].set_color('black')
		plt.pause(0.1)
		if x >= high:
			rects[high_index].set_color('black')
			rects[i].set_color('red')
			plt.pause(0.1)
			high, high_index = x, i
		if i == len(list) - 1 and i != high_index:
			rects[i].set_color('black')

list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Highest Number")
find(list)
plt.show()
			