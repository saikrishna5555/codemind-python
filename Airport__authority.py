n=int(input())
d=[]
for i in range(n):
    a=int(input())
    d.append(a)
t=int(input())
s=0
for i in d:
    if i<=t:
        s+=1
    else:
        s+=2
print(s)
    