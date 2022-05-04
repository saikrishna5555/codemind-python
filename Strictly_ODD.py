def strictly_odd(d):
    n=len(d)
    for i in range(n):
        if i%2==0:
            if d[i]%2:
                return False
    return True
n=int(input())
d=list(map(int,input().split()))
res=strictly_odd(d)
print(res)