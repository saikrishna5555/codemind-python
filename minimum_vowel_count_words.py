def vowel(s):
    a='aeiou'
    c=0
    for i in s:
        if i in a:
            c+=1
    return c
s=input()
s=s.split()
e=[]
for i in s:
    a=vowel(i)
    e.append(a)
m=min(e)
c=0
for i in e:
    if i==m:
        c+=1
print(c)