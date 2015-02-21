#encoding:utf-8
__metaclass__=type
def d(n):
	n_b= sum([i for i in xrange(1,n) if n%i==0])
	#n的因子和
	n_b_n= sum([i for i in xrange(1,n_b) if n_b%i==0])
	#n的因子和的因子和
	if n==n_b_n and n_b_n !=n_b:
		return n_b+n_b_n
	else:
		return False
print d(220)
a=[]
for n in range(4,10000):
	if d(n):
		a.append(d(n))
print sum(a)/2