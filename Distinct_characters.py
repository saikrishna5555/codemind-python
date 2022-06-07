n=input()
n=n.lower()
d=list(n)
e=[]
for i in d:
    if i==' ':
        continue
    elif d.count(i)==1:
        e.append(i)
e=sorted(e)
e=''.join(e)
print(e)