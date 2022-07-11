from math import *
def prime(n):
    sq=int(sqrt(n))
    if n==1:
        return False
    for i in range(2,sq+1):
        if n%i==0:
            return False
    return True
n=int(input())
e=[]
p=1
for i in range(2,n):
    if n%i==0:
        if prime(i):
            e.append(i)
for i in e:
    p*=i
if p==n:
    print(*e)
else:
    print(-1)