def last_odd(d):
    n=len(d)
    a=d[::-1]
    for i in range(n):
        if a[i]%2:
            return a[i]
n=int(input())
d=list(map(int,input().split()))
res=last_odd(d)
print(res)