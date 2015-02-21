#encoding:utf-8
import math
"""
方法1：耗时22s
"""
def is_prime(n):
	if n==1:
		return False	
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	else:
		return True
print is_prime(6)

# def sum_():
# 	s=0
# 	for i in range(1,2000001):
# 		if is_prime(i):
# 			s+=i
# 	else:
# 		print s
print sum(filter(is_prime,xrange(3,2000001,2)))+2
"""
方法2：0.7s
"""
# def getPrimesUntilN(n):
#     numList = range(2,n+1,1)
#     i = 2
#     nroot = n ** 0.5
#     while i < nroot:
#         if numList[i]:
#             j = i ** 2
#             while j < n-1:
#                 numList[j] = 0
#                 j = j + i
#         i = i + 1
#     return [k for k in range(2, n-1) if numList[k]]

# print sum(getPrimesUntilN(2000000))