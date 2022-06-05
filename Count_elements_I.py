n,m=map(int,input().split())
d=list(map(int,input().split()))
d1=list(map(int,input().split()))
e=[]
c=0
for i in d:
    if i in d1:
        e.append(i)
a=[]
for i in e:
    if i not in a:
        a.append(i)
        c+=1
print(c)