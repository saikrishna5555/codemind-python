n=int(input())
d=list(map(int,input().split()))
ec=int(input())
e=[]
m=max(d)
for i in d:
    if i+ec>=m:
        e.append(True)
    else:
        e.append(False)
print(*e)