n=int(input())
d=list(map(int,input().split()))
t=int(input())
if t in d:
    print(d.index(t))
else:
    print(-1)