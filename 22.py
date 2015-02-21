#encoding:utf-8
__metaclass__=type
def a_p(name):
	m=0
	for i in name:
		if ord(i)>34:
			#除去字符串中的双引号
			m+=ord(i)-64
			#利用ASCII求得i的位置并且求和
	return m
def values(name):
	s=0
	for i in xrange(1,len(name)+1):
		s+=a_p(name[i-1])*i
	return s
if __name__=="__main__":
	names=sorted(open("E:\\names.txt").readline().split(","),key=str.upper)
	#将从小到大排序,sorted()不影响a本身结构
	#a.sort() 已改变a的结构，b = a.sort() 是错误的写法! 
	#str.split()方法将字符串分解为列表
	#list.join()方法将类表合并成字符串
	print values(names)
