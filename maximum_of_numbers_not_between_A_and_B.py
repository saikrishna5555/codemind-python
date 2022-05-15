n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
ds=max(d)
f=[]
s=0
for i in d:
    if i>=a and i<=b:
        f.append(i)
fs=max(f)
if fs==ds:
    print(-1)
else:
    print(ds)