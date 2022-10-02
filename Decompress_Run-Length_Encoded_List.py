n=int(input())
d=list(map(int,input().split()))
e=[]
for i in range(0,len(d)-1,2):
    a=d[i]
    b=d[i+1]
    em=[]
    em.append(b)
    r=em*a
    e+=r
print(*e)
    