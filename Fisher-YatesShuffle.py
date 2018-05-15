"""Fisher-Yates Visualization"""

import matplotlib.pyplot as plt
import numpy as np
import random

def shuffle(list):
	n = len(list)
	j = 1
	for i in range(0, n-2):
		j = np.random.randint(i, n)
		rects[i].set_color('red')
		if i > 0 or i == n-3: rects[i-1].set_color('black')
		list[i], list[j] = list[j], list[i]
		for rect, h in zip(rects, list):
			rect.set_height(h)
		plt.pause(0.05)
	rects[n-3].set_color('black')
		
n = 50
list = list(range(n))
rects = plt.bar(np.arange(len(list)),list,
				align='edge',color='black',
				width=0.5)
shuffle(list)
plt.title("Fisher-Yates Shuffle")
plt.show()