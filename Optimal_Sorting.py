t=int(input())
for i in range(t):
    n=int(input())
    d=list(map(int,input().split()))
    a=sorted(d)
    if a==d:
        print(0)
    else:
        print(max(a)-min(a))