t=int(input())
for _ in range(t):
    n=int(input())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    r=p+q
    r=set(r)
    if len(r)==n:
        print('YES')
    else:
        print("NO")