"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


import math
def is_prim_num(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    else:
            return True

def prime():
        s=1
        i=2
        while s <=10001:
                   if is_prim_num(i):
                           s = s + 1
                           print i
                   i=i+1
prime()
