from math import *
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
a=int(input())
b=a-1
f=a+1
while True:
    if prime(a):
        print(0)
        break
    elif prime(b):
        print(abs(a-b))
        break
    elif prime(f):
        print(abs(a-f))
        break
    else:
        b-=1
        f+=1
        
    
    