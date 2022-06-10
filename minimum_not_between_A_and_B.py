n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
d1=[]
e=[]
c=0
for i in d:
    if i>=a and i<=b:
        e.append(i)
for i in d:
    if i not in e:
        d1.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(min(d1))