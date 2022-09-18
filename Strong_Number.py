def fac(n):
    p=1
    for i in range(1,n+1):
        p*=i
        
    return p
n=int(input())
t=n
s=0
while n:
    d=n%10
    f=fac(d)
    s+=f
    n=n//10
if t==s:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")