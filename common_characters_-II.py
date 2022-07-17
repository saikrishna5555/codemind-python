s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
e=[]
for i in s2:
    if i in s1:
        e.append(i)
for i in s1:
    if i in s2:
        e.append(i)
a=sorted(e)
b=[]
for i in a:
    if i==' ':
        continue
    if i not in b:
        b.append(i)
print(len(b))
