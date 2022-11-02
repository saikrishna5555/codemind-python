n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
s=0
for i in e:
    s+=sum(i)
print(s)