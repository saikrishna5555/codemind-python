def difference(d):
    n=len(d)
    es=0
    os=0
    for i in d:
        if i%2==0:
            es+=i
        else:
            os+=i
    a=max(es,os)
    b=min(es,os)
    diff=abs(a-b)
    return diff
        
n=int(input())
d=list(map(int,input().split()))
diff=difference(d)
print(diff)