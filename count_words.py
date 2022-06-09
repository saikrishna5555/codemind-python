s=input()
s=s.split()
v='aeiouAEIOU'
c=0
for i in s:
    if i[0] in v and i[-1] not in v:
        c+=1
print(c)