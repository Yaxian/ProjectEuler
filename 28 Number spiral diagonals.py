#encoding:utf-8
__metaclass__=type
m = [i for i in xrange(1,1001**2+1)]
p=0
t=0
for i in xrange(2,1001**2,2):
	i_p = 0
	while i_p<4:
		try:
			p+=i
			t+=m[p]
		except:
			pass
		i_p+=1
print t+1