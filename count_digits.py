n=int(input())
d=list(map(int,input().split()))
e=[]
b=[]
for i in d:
    if i<0:
        i=i*-1
    s=str(i)
    l=len(s)
    e.append(l)
print(*e)