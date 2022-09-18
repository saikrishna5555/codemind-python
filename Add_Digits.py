def digitsum(n):
    s=0
    while n:
        d=n%10
        s+=d
        n=n//10
    return s
n=int(input())
while n>10:
    n=digitsum(n)
print(n)