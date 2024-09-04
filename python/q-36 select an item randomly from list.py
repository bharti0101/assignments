#Write a Python program to select an item randomly from a list.

#method - 1 using random.choice from random library

import random
li = ['a', 'b', 2, 7, 8, 4]
a = random.choice(li)
print(a)

#method - 2 using numpy.random.choice

import numpy as np

li2 = [2, 7, 8, 4]
a = np.array(li2)
b = np.random.choice(a)
print(b)