n=input()
n=n.split()
s=n[-1]
m=min(s)
l=m.lower()
if l in s:
    print(l)
else:
    print(m)