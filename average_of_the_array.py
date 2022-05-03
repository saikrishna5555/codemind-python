def average(d):
    s=sum(d)
    l=len(d)
    res=s/l
    p=format(res,'.2f')
    return p



n=int(input())
d=list(map(int,input().split()))
res=average(d)
print(res)