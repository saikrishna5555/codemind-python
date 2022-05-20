def vowels(d):
    c=0
    for i in d:
        if i in d1:
            c+=1
    return c



n=input()
v='aeiouAEIOU'
d1=list(v)
s=n.split()
d=list(s)
a=[]
for i in d:
    if vowels(i):
        a.append(vowels(i))
print(*a)