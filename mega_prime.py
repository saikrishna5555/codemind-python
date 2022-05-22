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
d1=[]
c=0
if prime(n):
    while n:
        d=n%10
        d1.append(d)
        n=n//10
    
    for i in d1:
        if prime(i):
            c+=1
        else:
            print("Not Mega Prime")
            break
    if len(d1)==c:
        print("Mega Prime")
else:
    print("Not Mega Prime")