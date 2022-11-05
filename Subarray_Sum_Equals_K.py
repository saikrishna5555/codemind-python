n,k=map(int,input().split())
d=list(map(int,input().split()))
e=[]
for i in range(n+1):
    for j in range(0,i):
        a=d[j:i]
        e.append(a)
c=0
for i in e:
    s=sum(i)
    if s==k:
        c+=1
print(c)