s=input()
d=[]
for i in s:
    if i.isalpha():
        d.append(i)
d.reverse()
for i in range(len(s)):
    if s[i].isalpha()==False:
        d.insert(i,s[i])
print(''.join(d))