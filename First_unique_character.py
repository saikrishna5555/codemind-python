n=input()
d=list(n)
c=0
for i in d:
    if d.count(i)==1:
        c+=1
        print(i)
        break
if c==0:
    print(-1)