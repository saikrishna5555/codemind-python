n,m=map(int,input().split())
d=list(map(int,input().split()))
d1=list(map(int,input().split()))
e=[]
for i in d:
    if i in d1:
        e.append(i)
a=[]
for i in e:
    if i not in a:
        a.append(i)
print(*a)