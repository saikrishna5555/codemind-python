n=input()
d=list(n)
v='aeiouAEIOU'
e=[]
c=0
a=[]
for i in d:
    if i in v:
        e.append(i)
        c+=1
for i in e:
    if i not in a:
        a.append(i)
if c==0:
    print("-1")
else:
    print(*a)