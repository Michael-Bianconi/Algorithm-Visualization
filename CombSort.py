"""Comb Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random, math

def sort(list):
	
	gap = len(list)
	shrink = 1.3 #ideal shrink size according to algorithm creator
	sorted = False
	
	while sorted is False:
		gap = math.floor(gap / shrink)
		
		if gap > 1:
			sorted = False #gap means unsorted
		
		else:
			gap = 1
			sorted = True #done
		
		i = 0
		while i+gap < len(list):
			if list[i] > list[i+gap]:
				swap(list, i, i+gap)
				for rect, h in zip(rects, list):
					rect.set_height(h)
		
				plt.pause(0.01)
				sorted = False
				
			i += 1

def swap(list, a, b):
	list[a], list[b] = list[b], list[a]
	
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
sort(list)
plt.show()