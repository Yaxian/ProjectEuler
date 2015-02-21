#encoding:utf-8
__metaclass__=type
def f(n):
	a=len(repr(n))

def cycle_len(x):
  cyclic = []
  num = 1
  while (num not in cyclic):
    cyclic.append(num)
    num = (num*10)%x
  return len(cyclic)-cyclic.index(num)


ans = [0]
for i in range (1,1000): ans.append(cycle_len(i))
print ans.index(max(ans))