def reverse(d):
    d=d[::-1]
    return d

n=input()
d=n.split()
a=[]
b=[]
for i in d:
    i=reverse(i)
    a.append(i)
a=reverse(a)
print(*a)