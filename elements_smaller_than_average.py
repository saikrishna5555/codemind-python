def avg(d):
    n=len(d)
    a=sum(d)
    avg=0
    c=0
    avg=a//n
    for i in range(n):
        if d[i]<=avg:
            c+=1
    return c
n=int(input())
d=list(map(int,input().split()))
res=avg(d)
print(res)