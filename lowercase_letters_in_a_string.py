n=input()
d=list(n)
c=0
for i in d:
    if i.islower():
        c+=1
print(c)