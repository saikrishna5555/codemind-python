def last_even(d):
    n=len(d)
    a=d[::-1]
    for i in range(n):
        if a[i]%2==0:
            return a[i]
n=int(input())
d=list(map(int,input().split()))
res=last_even(d)
print(res)