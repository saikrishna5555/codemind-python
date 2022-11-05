s=input()
s=s.split()
mis=0
mxs=0
e=[]
for i in s:
    mis=ord(min(i))
    mxs=ord(max(i))
    a=abs(mis-mxs)
    e.append(a)
print(*e)