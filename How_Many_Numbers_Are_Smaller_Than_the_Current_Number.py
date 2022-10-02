def small(d,i):
    c=0
    for j in d:
        if j<i:
            c+=1
    return c
n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    a=small(d,i)
    e.append(a)
print(*e)