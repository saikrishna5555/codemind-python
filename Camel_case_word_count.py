s=input()
s=s[1:]
c=1
d=list(s)
for i in d:
    if i==i.upper():
        c+=1
print(c)