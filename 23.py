#encoding:utf-8
__metaclass__=type
"""
Non-abundant sums
"""
# import math
# def isAbunt(n):
# 	list_div=[]
# 	for i in xrange(1,int(math.sqrt(n))+1):
# 		if n%i==0:list_div.extend([i]+[n/i])
# 	if n in list_div:del(list_div[1])
# 	if sum(list_div)>n:
# 		return 0
# 	else:
# 		return n
import math
def findDivisors(num):
    divisors = [1]
    limit = int (math.sqrt(num)) + 1
    for f in range(2,limit):
        if num % f == 0:
            divisors.append(f)
            f2 = num // f
            if f * f2 == num:
                if not f2 in divisors:
                    divisors.append(f2)
    return divisors

def findAbundantNumbers(limit):
    abundantNumbers = []
    for num in range (1, limit):
        divisors = findDivisors(num)
        divisorSum = sum(divisors)
        if divisorSum > num:
            abundantNumbers.append(num)
    return abundantNumbers

def myMain(argv):
    limit = 28123
    abundant = findAbundantNumbers(limit)
    numbers = set([])
    for n1 in range(1,limit):
        numbers.add(n1)
    abundantSums = set([])
    for n1 in range(0, len(abundant)):
        for n2 in range(n1, len(abundant)):
            pairSum = abundant[n1] + abundant[n2]
            if (pairSum < limit):
                abundantSums.add(pairSum)
    qualifyingNumbers = numbers - abundantSums;
    print sum(qualifyingNumbers)

if __name__ == "__main__":
    import sys
    myMain(sys.argv)