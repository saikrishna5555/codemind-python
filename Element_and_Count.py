n=int(input())
d=list(map(int,input().split()))
b=[]
e=[]
for i in d:
    if i not in b:
        b.append(i)
for i in b:
    e.append(i)
    e.append(d.count(i))
print(*e)