def reverse(n):
    rev=0
    temp=n
    p=-1
    if n<0:
        n=n*p
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    if temp<0:
        return -rev
    return rev
n=int(input())
res=reverse(n)
print(res)