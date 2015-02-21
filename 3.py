#encoding:utf-8
import math

def prime_factor_sqrt(n=600851475143,i=1):
    """
        为什么循环范围定在平方根呢？：因为一个数的因子是成对的，a=b*c。也就是说：找到一个因子b，肯定会找到相对应的另外一个因子c（a/b）。所以我们的工作量减少了一半。
        又有：一个因子变大，另一个因子必然要变小。假设b永远是小的那个，c是大的那个，那么b的最大值就是a的平方根。也就是b=c=(根号a)的时候。所以循环范围定在[1 , a的平方根+1]，+1的原因是为了能够取到a的平方根避免遗漏。
    """
    prime_factor = []
    n = int(math.sqrt(n))
    while i<n:
        if 600851475143%i ==0:
            prime_factor.append(i)
            prime_factor_sqrt(600851475143%i)
        i+=1
    s=1
    for k in prime_factor:
        s=s*k
        if s ==600851475143:
          print k
          break
