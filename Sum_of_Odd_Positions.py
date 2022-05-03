def odd_sum(d):
    n=len(d)
    os=0
    for i in range(n):
        if i%2:
            os+=d[i]
    return os

n=int(input())
d=list(map(int,input().split()))
os=odd_sum(d)
print(os)