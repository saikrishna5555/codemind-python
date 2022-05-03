def last_index(d):
    n=len(d)
    c=0
    for i in range(n):
        if d[i]%2:
            c=i
    return c
n=int(input())
d=list(map(int,input().split()))
res=last_index(d)
print(res)