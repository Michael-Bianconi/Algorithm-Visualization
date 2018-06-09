"""Stooge Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random

def sort(list):
	
    recursive_sort(list, 0, len(list)-1)
    
def recursive_sort(list, start, end):
    if list[start] > list[end]:
        list[start], list[end] = list[end], list[start]
        for rect, h in zip(rects, list):
            rect.set_height(h)
        plt.pause(0.01)
    
    if (end - start + 1) > 2:
        new_end = int((end - start + 1) / 3)
        recursive_sort(list, start, end-new_end)
        recursive_sort(list, start+new_end, end)
        recursive_sort(list, start, end-new_end)
        
    return list
			
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Stooge Sort")
sort(list)
plt.show()