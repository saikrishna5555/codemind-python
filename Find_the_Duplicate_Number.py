n=int(input())
d=list(map(int,input().split()))
s=set(d)
for i in s:
    if d.count(i)!=1:
        print(i)
