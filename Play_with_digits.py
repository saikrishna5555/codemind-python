def su(n):
    s=0
    while n:
        d=n%10
        n=n//10
        s+=d
    return s
n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    a=su(i)
    e.append(a)
print(sum(e))