'''
Janze
2021/10/14
project euler problem #1: https://projecteuler.net/problem=1
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
  Find the sum of all the multiples of 3 or 5 below 1000.
'''
import numpy as np
# what is numpy https://numpy.org/doc/stable/user/whatisnumpy.html

x = np.arange(1, 1000)
# 'x' is you variable; 'np' is your call to numpy
# what is 'arange' https://realpython.com/how-to-use-numpy-arange/

### find multiple of 3 using modulo == 0
n3 = x[(x % 3 == 0)]
# the vaiable 'n3' will be your output list of numbers; 
# the variable 'x' refers the list to 'arange(1, 1000)'
# what is modulo https://en.wikipedia.org/wiki/Modulo_operation
# how is it used in python https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved
print(n3[:1000])
# print out the list 'n3'

### find  multiple of 5 using modulo == 0
n5 = x[(x % 5 == 0)]
print(n5[:1000])
# same procedure as above for 3

### find multiple of 3 or 5 using modulo
n = x[(x % 3 == 0) | (x % 5 == 0)]
# what is "|" https://www.freecodecamp.org/news/basic-operators-in-python-with-examples/
print(n[:1000])
# print sum the numbers
print(n.sum())


'''
# original code from https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-68.php
import numpy as np
x = np.arange(1, 100)
# find multiple of 3 or 5
n = x[(x % 3 == 0) | (x % 5 == 0)]
print(n[:1000])
# print sum the numbers
print(n.sum())
'''