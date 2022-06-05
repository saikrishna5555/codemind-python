s1=input()
s2=input()
s1=s1.upper()
s2=s2.upper()
c=0
s1=s1.split()
s2=s2.split()
e=[]
for i in s1:
    if i in s2:
        e.append(i)
for i in s2:
    if i in s1:
        e.append(i)
a=[]
for i in e:
    if i not in a:
        a.append(i)
        c+=1
print(c)