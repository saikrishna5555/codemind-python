n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
e=[]
c=0
for i in d:
    if i>=a and i<=b:
        e.append(i)
        c+=1
if c==0:
    print("-1")
else:
    print(min(e))