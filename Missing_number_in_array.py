t=int(input())
for i in range(t):
    n=int(input())
    d=list(map(int,input().split()))
    n=(n*(n+1))//2
    s=sum(d)
    print(n-s)