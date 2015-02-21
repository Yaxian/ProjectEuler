#encoding:utf-8
__metaclass__=type
def f(n):
	"""
	用递归描述程序很简单，但效率低下，而且，当递归的深度达到一定数量时，
	肯定会发生堆栈溢出。

	因此，迭代可以优化递归。
	"""
	if n==1 or n==2:
		return 1
	else:
		return f(n-2)+f(n-1)

def i_f(n):
	a,b=0,1
	while len(repr(b))<=n:
		yield b
		a,b=b,a+b
print len(map(int,i_f(1000)))+1