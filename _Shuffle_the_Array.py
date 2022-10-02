n=int(input())
d=list(map(int,input().split()))
h=n//2
a=d[0:h]
b=d[h:]
e=[]
for i in range(h):
    e.append(a[i])
    e.append(b[i])
print(*e)