"""Selection Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list):
	n = len(list)
	
	for j in range(0,n-1):
		imin = j
		for i in range(j+1,n):
			if list[i] < list[imin]:
				imin = i
		#swap
		if imin != j:
			list[j],list[imin] = list[imin],list[j]
			for rect, h in zip(rects, list):
				rect.set_height(h)
			plt.pause(0.01)
			
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Selection Sort")
sort(list)
plt.show()