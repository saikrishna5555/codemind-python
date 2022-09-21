from math import *
n=int(input())
sq=int(sqrt(n))
s=0
for i in range(1,sq+2):
    if 2**i==n:
        print(0)
        break
    elif 2**i>n:
        a=n-(2**(i-1))
        b=abs(n-2**i)
        if a<b:
            print(a)
        else:
            print(b)
        break
    