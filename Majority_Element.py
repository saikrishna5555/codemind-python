n=int(input())
d=list(map(int,input().split()))
a=n//2
s=set(d)
for i in s:
    if d.count(i)>a:
        print(i)
        break
