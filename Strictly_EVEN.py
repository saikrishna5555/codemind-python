def strictly_even(d):
    n=len(d)
    for i in range(n):
        if i%2:
            if d[i]%2==0:
                return False
    return True
n=int(input())
d=list(map(int,input().split()))
res=strictly_even(d)
print(res)