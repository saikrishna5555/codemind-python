n=int(input())
d=list(map(int,input().split()))
a=sorted(d)
if d==a[::-1]:
    print("yes")
else:
    print("no")