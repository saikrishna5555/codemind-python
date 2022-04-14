n=int(input())
s=0
q=n
n=n**2

while n:
    d=n%10
    n=n//10
    s=s+d
   
if q==s:
    print("Neon Number")
else:
    print("Not Neon Number")
    