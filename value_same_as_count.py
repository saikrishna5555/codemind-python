n=int(input())
d=list(map(int,input().split()))
s=set(d)
d1=list(s)
c=0
for i in d1:
    if i==d.count(i):
        c+=1
print(c)