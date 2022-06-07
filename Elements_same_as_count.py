n=int(input())
d=list(map(int,input().split()))
b=[]
e=[]
c=0
for i in d:
    if i not in b:
        b.append(i)
for i in b:
    if i==d.count(i):
        e.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(*e)