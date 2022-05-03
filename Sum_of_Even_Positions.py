def even_sum(d):
    n=len(d)
    es=0
    for i in range(n):
        if i%2==0:
            es+=d[i]
    return es    

n=int(input())
d=list(map(int,input().split()))
es=even_sum(d)
print(es)