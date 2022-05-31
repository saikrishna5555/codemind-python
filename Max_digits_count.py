n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    s=str(i)
    l=len(s)
    e.append(l)
m=max(e)
print(e.count(m))