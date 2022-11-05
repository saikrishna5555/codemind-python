n=int(input())
d=list(map(int,input().split()))
r=list(map(int,input().split()))
ds=sum(d)
rs=sum(r)
if ds>=rs:
    print(0)
else:
    print(sum(r)-sum(d))