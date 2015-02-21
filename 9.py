#encoding:utf-8
"""
A Pythagorean triplet(毕达哥拉斯三元数组) is a set of three natural numbers, 
a < b < c, for which,

a**2 + b**2 = c**2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a*b*c.
"""

for a in range(1,500):
	for b in range(a,500):
		if (a**2 +b**2 == (1000-a-b)**2 and b<1000-a-b):
			print a*b*(1000-a-b)