n=int(input())
d=list(map(int,input().split()))
k=int(input())
s=set(d)
d1=list(s)
a=[]
h=0
for i in d1:
    if k==d.count(i):
        a.append(i)
        h=1
if h==0:
    print(-1)
else:
    print(*a)