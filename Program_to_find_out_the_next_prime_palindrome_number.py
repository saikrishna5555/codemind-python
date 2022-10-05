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
a+=1
while True:
    s=str(a)
    if s==s[::-1]:
        if prime(a):
            print(a)
            break
        else:
            a+=1
    else:
        a+=1