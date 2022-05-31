n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    s=str(i)
    l=len(s)
    e.append(l)
m=min(e)
print(e.count(m))