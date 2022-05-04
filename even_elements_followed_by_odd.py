n=int(input())
d=list(map(int,input().split()))
l=[]
a=0
for i in d:
    if i%2==0:
        a=l.append(i)
for i in d:
    if i%2:
        a=l.append(i)
print(*l)