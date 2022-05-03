def even(d):
    n=len(d)
    c=0
    for i in range(n):
        if d[i]%2==0:
            c=i            
    return c
    

n=int(input())
d=list(map(int,input().split()))
res=even(d)
print(res)