n=input()
n=n.lower()
d=list(n)
d=sorted(d)
e=[]
for i in d:
    if i==' ':
        continue
    elif i not in e:
        e.append(i)
e=''.join(e)
print(e)