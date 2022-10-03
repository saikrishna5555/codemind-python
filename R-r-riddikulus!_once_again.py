n,m=map(int,input().split())
d=list(map(int,input().split()))
m=m%n
for i in range(m):
    a=d.pop(0)
    d.append(a)
print(*d)