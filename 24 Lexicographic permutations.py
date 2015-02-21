#encoding:utf-8
__metaclass__=type
import itertools
print "".join(list(itertools.permutations(map(str,range(10)),10))[10**6-1])
