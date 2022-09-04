n=int(input())
d=list(map(int,input().split()))
e=[]
for i in range(0,n-1,2):
    e.append(d[i])
    e.append(d[i+1])
if n%2:
    e.append(d[-1])
    e.append(0)
print(*e)