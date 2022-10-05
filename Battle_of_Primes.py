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
b=int(input())
co=1
r=a+b+1
while prime(r)==False:
    r+=1
    co+=1
print(co)
    
