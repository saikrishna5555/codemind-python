t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    if k!=n:
        k=k%n
    for i in range(k):
        a=s[0:k]
        b=s[k::]
        a=a[::-1]
        s=a+b
        k-=1
    print(s)
