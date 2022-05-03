def even_sum(d):
    n=len(d)
    es=0
    for i in d:
        if i%2==0:
            es+=i
    return es

n=int(input())
d=list(map(int,input().split()))
s=even_sum(d)
print(s)