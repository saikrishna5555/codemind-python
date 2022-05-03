def avg(d):
    s=sum(d)
    l=len(d)
    res=s//l
    return res


n=int(input())
d=list(map(int,input().split()))
res=avg(d)
if res in d:
    print("True")
else:
    print("False")