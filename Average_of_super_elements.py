n=int(input())
d=list(map(int,input().split()))
s=set(d)
e=[]
for i in s:
    if i not in e:
        if i==d.count(i):
            e.append(i)
            e.append(d.count(i))
if len(e)!=0:
    su=sum(e)
    l=len(e)
    avg=su/l
    print(format(avg,".2f"))
else:
    print("-1")