n=int(input())
d=list(map(int,input().split()))
e=[]
c=0
for i in range(1,n):
    a=d[i:]
    if len(a)==0:
        break
    else:
        m=max(a)
        e.append(m)
e.append(-1)
print(*e)