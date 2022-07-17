s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split()
s2=s2.split()
e=[]
for i in s2:
    if i in s1:
        e.append(i)
print(*e)