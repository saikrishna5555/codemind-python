n=int(input())
t=int(input())
e=[]
while n:
    a=n%t
    e.append(a)
    n=n//t
i=0
j=0
m=0
while j!=len(e):
    if e[j]==0:
        m=max(m,j-i+1)
        j+=1
    else:
        j+=1
        i=j
if m==0:
    print(-1)
else:
    print(m)