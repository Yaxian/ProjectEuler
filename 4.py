#encoding:utf-8
"""
A palindromic number （回文数）reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math
palindromic_number = []
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			palindromic_number.append(a*100000+b*10000+c*1000+c*100+b*10+a)
palindromic_number.reverse()
#首先找出所有的回文数，然后再判断是否是2个三位数相乘的结果
for k in palindromic_number:
	for prime_factor in range(100,int(math.sqrt(k))):
		if k%prime_factor==0 and k/prime_factor <1000:
			print k,
			break
