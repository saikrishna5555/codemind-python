n=int(input())
s=0
p=1
while n:
    d=n%10
    n=n//10
    s=s+d
    p=p*d
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")