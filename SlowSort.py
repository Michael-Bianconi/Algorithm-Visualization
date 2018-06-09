"""Stooge Sort Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random
from math import floor

def sort(list):
	recursive_sort(list,0,len(list)-1)
    
def recursive_sort(a,i,k):
    if i >= k: return
    m = floor((i+k)/2)
    
    print('%s, %s, %s' % (i,k,m))
    
    recursive_sort(a,i,m)
    recursive_sort(a,m+1,k)
    if a[k] < a[m]:
        a[k], a[m] = a[m], a[k]
        for rect, h in zip(rects, list):
            rect.set_height(h)
        plt.pause(0.01)
    recursive_sort(a,i,k-1)
			
list = random.sample(range(1, 101), 50)
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
plt.title("Slow Sort")
sort(list)
plt.show()