def summ(n):
    s=0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s
d1=input()
d1=list(d1)
e=[]
d=[]
for i in range(0,len(d1),2):
    i=int(d1[i])
    d.append(i)
for i in d:
    i=int(i)
    s=summ(i)
    if s in d:
        e.append(i)
if len(e)==0:
    print(-1)
else:
    print(*sorted(e))