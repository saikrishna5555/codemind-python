n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
r=[]
for i in e:
    s=sum(i)
    r.append(s)
print(max(r))