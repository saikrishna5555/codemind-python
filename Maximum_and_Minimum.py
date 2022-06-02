n=int(input())
d=list(map(int,input().split()))
s=set(d)
e=[]
for i in s:
    if i not in e:
        if i==d.count(i):
            e.append(i)
if len(e)!=0:
    print(min(e),max(e))
    
else:
    print("-1")