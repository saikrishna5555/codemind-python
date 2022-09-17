n,x=map(int,input().split())
s=str(n)
l=len(s)
a=n//(10**(l-x))
b=n%10**x
print(abs(a-b))