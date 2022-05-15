n=int(input())
d=list(map(int,input().split()))
a,b=map(int,input().split())
f=[]
s=0
for i in d:
    if i<a or i>b:
        f.append(i)
s=sum(f)
print(s)