n=input()
d=list(n)
c=0
for i in d:
    if i.isupper():
        c+=1
print(c)