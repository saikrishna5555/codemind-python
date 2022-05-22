from math import *
def prime(n):
    sq=int(sqrt(n))
    if n==1 :
        return False
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
temp=n
rev=0
while n:
    d=n%10
    rev=rev*10+d
    n=n//10
if prime(temp) and prime(rev):
    print("circular prime")
elif prime(temp) or prime(rev):
    print("prime but not a circular prime")
else:
    print("not prime")