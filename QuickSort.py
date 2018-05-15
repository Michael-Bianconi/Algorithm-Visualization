"""Quick Sort Visualizations

	Quick Sort uses a divide and conquer algorithm.
	It divides the given list into two smaller lists,
	one for high values and one for low values. It then
	recursively calls itself on those smaller lists.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list, low, high):
	if low < high:
		p = partition(list, low, high)
		sort(list, low, p - 1)
		sort(list, p + 1, high)
		
def partition(list, low, high):

	pivot = list[high]
	i = low - 1
	for j in range(low, high):
	
		if list[j] < pivot:
			i += 1
			swap(list, i, j)
			
			for rect, h in zip(rects, list):
				rect.set_height(h)
			plt.pause(0.01)
			
	swap(list, i+1, high)
	
	for rect, h in zip(rects, list):
		rect.set_height(h)
		
	plt.pause(0.01)
	return i + 1
	
def swap(list, a, b):
	list[a], list[b] = list[b], list[a]
	
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
sort(list, 0, len(list)-1)
plt.show()