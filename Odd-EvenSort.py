"""Odd-Even Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list):
	sorted = False
	while sorted is False:
		sorted = True
		#Odd
		for i in range(1, len(list)-1, 2):
			if list[i] > list[i+1]:
				list[i],list[i+1] = list[i+1],list[i]
				
				for rect, h in zip(rects, list):
					rect.set_height(h)
				plt.pause(0.01)
				
				sorted = False
		#Even
		for i in range(0, len(list)-1, 2):
			if list[i] > list[i+1]:
				list[i],list[i+1] = list[i+1],list[i]
				
				for rect, h in zip(rects, list):
					rect.set_height(h)
				plt.pause(0.01)
				
				sorted = False
				
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Odd-Even Sort")
sort(list)
plt.show()