n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
c=0
for i in e:
    a=sorted(i)
    if a==i or a==i[::-1]:
        c+=1
print(c)