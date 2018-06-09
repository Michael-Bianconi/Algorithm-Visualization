"""Gnome Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list):
	
    i = 0
    while i < len(list):
        if i == 0 or list[i] >= list[i-1]:
            i += 1
        else:
            list[i], list[i-1] = list[i-1], list[i]
            for rect, h in zip(rects, list):
                rect.set_height(h)
            plt.pause(0.01)
            i -= 1
			
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Gnome Sort")
sort(list)
plt.show()