n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
s=0
e1=[]
for i in range(m):
    for j in range(n):
        s+=e[j][i]
    e1.append(s)
    s=0
print(*e1)