from math import *
n=int(input())
d=list(map(int,input().split()))
s=0
for i in d:
    sq=int(sqrt(i))
    if sq*sq==i:
        s+=i
print(s)