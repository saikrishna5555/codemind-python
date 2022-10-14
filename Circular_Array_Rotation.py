n,k,q=map(int,input().split())
a=list(map(int,input().split()))
k=k%n
for i in range(k):
    p=a.pop()
    a.insert(0,p)
for _ in range(q):
    m=int(input())
    print(a[m])