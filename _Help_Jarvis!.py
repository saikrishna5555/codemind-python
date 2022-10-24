t=int(input())
for _ in range(t):
    n=int(input())
    r=[int(i) for i in str(n)]
    r=sorted(r)
    f=True
    for i in range(len(r)-1):
        if r[i]+1!=r[i+1]:
            print('NO')
            f=False
            break
    if f:
        print("YES")