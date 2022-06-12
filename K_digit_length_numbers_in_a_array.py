n,k=map(int,input().split())
d=list(map(int,input().split()))
c=0
for i in d:
    if i<0:
        i=i*-1
    a=str(i)
    l=len(a)
    if l==k:
        c+=1
print(c)