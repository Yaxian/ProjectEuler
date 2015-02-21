#encoding:utf-8
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
"""
方法1：
def chain(n,i=1):
	if n!=1:
		if n%2==0:
			return chain(n/2,i+1)
		else:
			return chain(3*n+1,i+1)
	else:
		return i
start_n=2
max_chain=0
while start_n<=1000000:
	if max_chain<=chain(start_n):
		max_chain=chain(start_n)
		star_max=start_n
	start_n+=1
print star_max,chain(star_max)
"""
"""
方法2：
"""
def next(n):
	if n%2 :
		return 3*n+1
	else:
		return n/2

class ChainCache:
	def __init__(self):
		self.cache = {}
	
	def __call__(self,n):
		if n==1:
			return 1
		elif n in self.cache:
			return self.cache[n]
		else:
			c = self.__call__(next(n))
			self.cache[n]=c+1
			return c+1

chainlen=ChainCache()
def maxlen(x):
	m=0
	v=0
	for i in xrange(1,x):
		l=chainlen(i)
		if l>m:
			m=l
			v=i
	return v,m
print maxlen(10**6)