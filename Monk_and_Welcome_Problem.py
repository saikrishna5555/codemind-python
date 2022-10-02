n=int(input())
d=list(map(int,input().split()))
a=list(map(int,input().split()))
e=[]
for i in range(n):
    e.append(d[i]+a[i])
print(*e)