"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
"""
def fun(n=1,s=0,a=0):

    if n <=100:
        s +=n
        a+=pow(n,2)
        return fun(n+1,s,a)
    else:
        print s**2-a
fun()
