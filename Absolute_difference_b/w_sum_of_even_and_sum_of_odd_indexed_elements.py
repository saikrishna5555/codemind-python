def sum_diff(d):
    n=len(d)
    es=0
    os=0
    for i in range(n):
        if i%2==0:
            es+=d[i]
        else:
            os+=d[i]
    a=max(es,os)
    b=min(es,os)
    diff=a-b
    return diff

n=int(input())
d=list(map(int,input().split()))
diff=sum_diff(d)
print(diff)