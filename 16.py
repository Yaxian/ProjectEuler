#encoding:utf-8
s=str(2**1000);
a=0
for i in s:
	a+=int(i)
print a

print sum(map(int,str(2**1000)))