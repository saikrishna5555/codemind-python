def count(d):
    c=0
    for i in d:
        if a==i:
            c+=1
    return c

n=int(input())
d=list(map(int,input().split()))
a=int(input())
c=count(d)
print(c)