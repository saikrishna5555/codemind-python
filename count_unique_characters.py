n=input()
n=n.lower()
d=list(n)
c=0
for i in d:
    if i==' ':
        continue
    elif d.count(i)==1:
        c+=1
print(c)