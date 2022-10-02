def even(n):
    c=0
    while n:
        d=n%10
        c+=1
        n=n//10
    return c
n=int(input())
d=list(map(int,input().split()))
c=0
for i in d:
    if even(i)%2==0:
        c+=1
print(c)