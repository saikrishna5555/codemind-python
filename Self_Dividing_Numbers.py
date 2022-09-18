def sel(n):
    t=n
    while n:
        d=n%10
        n=n//10
        if d==0:
            return False
        if t%d!=0:
            return False
    return True
n=int(input())
m=int(input())
e=[]
for i in range(n,m+1):
    if sel(i):
        e.append(i)
print(*e)