#encoding:utf-8
"""
Starting in the top left corner of a 2×2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import random
from math import factorial

# def c(n, k):
# 	return factorial(n) / factorial(k) / factorial(n - k)
# print c(4,2)
"""
需要注意的是，代码用到递归，当 值变大时，递归的次数以指数级别上升，
因此，要计算 r(20, 20) ，用这个方法效率是非常低的。
我们可以再将程序改进一下，像下面这样：
"""
def r(x, y):
	d = []
    	for i in range(y + 1):
		t = [0] * (x + 1)
		d.append(t)
	for iy in range(y + 1):
		for ix in range(x + 1):
			if ix == 0 and iy == 0:
				v = 0
			elif ix == 0 or iy == 0:
				v = 1
			else:
				v = d[iy - 1][ix] + d[iy][ix - 1]
			d[iy][ix] = v
	return d[y][x]
print r(20,20)