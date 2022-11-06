s1=input()
s2=input()
d=s1.split()
f=s2.split()
s1=set(d)
s2=set(f)
c=0
for i in s1:
    if i in s2:
        if d.count(i)==f.count(i):
            c+=1
print(c)