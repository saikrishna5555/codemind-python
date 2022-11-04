n=int(input())
t=n
for i in range(n):
    for j in range(n):
        print(t,end=' ')
        t-=1
    print()
    t=n
    