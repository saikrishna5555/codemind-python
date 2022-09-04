n=int(input())
d=list(map(int,input().split()))
e=[]
j=-1
for i in range(n//2):
    if i>=j:
        e.append(d[i])
        e.append(d[j])
        j-=1
if n%2:
    e.append(d[n//2])
    e.append(0)
print(*e)