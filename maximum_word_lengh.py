def count(n):
    d=list(n)
    l=len(d)
    return l

n=input()
s=n.split()
a=[]
for i in s:
    b=count(i)
    a.append(b)
l=max(a)
print(l)