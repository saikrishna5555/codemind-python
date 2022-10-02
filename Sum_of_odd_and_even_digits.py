n=int(input())
d=list(map(int,input().split()))
es=0
os=0
for i in range(n):
    if i%2==0:
        es+=d[i]
    else:
        os+=d[i]
if es-os==0:
    print("YES")
else:
    print("NO")