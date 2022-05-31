n=int(input())
d=list(map(int,input().split()))
e=[]
b=[]
for i in d:
    s=str(i)
    l=len(s)
    e.append(l)
m=max(e)
for i in d:
    s=str(i)
    if len(s)==m:
        b.append(i)
print(*b)
    