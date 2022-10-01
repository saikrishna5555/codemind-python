n=int(input())
d=list(map(int,input().split()))
s=set(d)
e=[]
for i in s:
    c=d.count(i)
    e.append(c)
c=0
for i in e:
    if i%2==0:
        c+=i//2
    else:
        i-=1
        c+=i//2
print(c)
        