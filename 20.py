#encoding:utf-8
__metaclass__=type
from math import factorial
#阶乘使用的factorial
s=str(factorial(100))
s_list=[]
for i in range(len(s)):
	s_list.append(s[i])
print sum(map(int,s_list))

print(sum([int(i) for i in str(factorial(100))])) 