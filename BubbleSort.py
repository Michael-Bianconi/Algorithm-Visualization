"""Bubble Sort Visualization

This application uses matplotlib to visualize Bubble Sort,
a common sorting algorithm.
"""
import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list,graph):
	n = len(list)
	for i in range(n):
		for j in range(n-i-1):
			if list[j] > list[j+1]:
				swap(list,j,j+1)
				for rect, h in zip(rects, list):
					rect.set_height(h)
				plt.pause(0.01)
		
def swap(list, a, b):
	list[a],list[b] = list[b],list[a]

list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
sort(list,rects)
plt.show()
