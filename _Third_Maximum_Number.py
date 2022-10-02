n=int(input())
d=list(map(int,input().split()))
s=set(d)
s=sorted(s)
if len(s)>=3:
    print(s[-3])
else:
    print(max(s))