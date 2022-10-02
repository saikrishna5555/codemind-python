t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    d=list(map(int,input().split()))
    k=k%n
    for i in range(k):
        a=d.pop()
        d.insert(0,a)
    print(*d)