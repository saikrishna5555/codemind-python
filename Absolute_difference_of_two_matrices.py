n=int(input())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
e1=[]
for i in range(n):
    d=list(map(int,input().split()))
    e1.append(d)
r=e[:][:]
for i in range(n):
    for j in range(n):
        r[i][j]=abs(e[i][j]-e1[i][j])
for i in r:
    print(*i)