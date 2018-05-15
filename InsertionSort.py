""" Insertion Sort Visualization

This application uses matplotlib to visualize Insertion Sort,
a common sorting algorithm.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list):
	i = 1

	for i in range(len(list)):
		
		j = i
		
		while j > 0 and list[j-1] > list[j]:
			swap(list, j, j-1)
			
			for rect, h in zip(rects, list):
				rect.set_height(h)
				
			plt.pause(0.01)
			j -= 1
		
		i += 1
		
def swap(list, a, b):
	list[a],list[b] = list[b],list[a]

list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
sort(list)
plt.show()
		