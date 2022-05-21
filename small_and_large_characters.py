n=input()
n=n.split()
d=list(n)
e=[]
for i in d:
    a,b=min(i),max(i)
    e.append(a)
    e.append(b)
print(*e)