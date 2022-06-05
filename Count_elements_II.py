n,m=map(int,input().split())
d=list(map(int,input().split()))
d1=list(map(int,input().split()))
e=[]
for i in d:
    if i not in d1:
        e.append(i)
for i in d1:
    if i not in d:
        e.append(i)
a=[]
c=0
for i in e:
    if i not in a:
        a.append(i)
        c+=1
print(c)
