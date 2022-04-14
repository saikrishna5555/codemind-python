n=int(input())
m=int(input())
ns=0
ms=0
for i in range(1,n+1):
    if n==i:
        break
    if n%i==0:
       ns=ns+i
for i in range (1,m+1):
    if m==i:
        break
    if m%i==0:
        ms+=i
if ms==n and ns==m:
    print("Amicable")
else:
    print("Not Amicable")
    