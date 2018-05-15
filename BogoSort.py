"""Bogo Sort Visualization

	A joke of a sorting algorithm, keep shuffling
	the list until it's sorted.
"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sorted(list):
	for i in range(1,len(list)):
		if list[i] <= list[i-1]:
			return False
	return True
	
def sort(list):
	while sorted(list) is False:
		random.shuffle(list)
		for rect, h in zip(rects, list):
			rect.set_height(h)
		plt.pause(0.2)
		
list = random.sample(range(1, 101), 5)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Bogo Sort")
sort(list)
plt.show()