from math import *
def prime(n):
    if n==0 or n==1:
        return False
    sq=int(sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
t=int(input())
for _ in range(t):
    n=int(input())
    a=n-1
    ad=0
    b=n+1
    bd=0
    while True:
        if prime(n):
            print(n)
            break
        if prime(a) and prime(b):
            if ad==bd:
                print(min(a,b))
                break
            elif ad<bd:
                print(a)
                break
            else:
                print(b)
                break
        elif prime(b):
            print(b)
            break
        elif prime(a):
            print(a)
            break
        else:
            a-=1
            ad+=1
            b+=1
            bd+=1