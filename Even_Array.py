def even_array(d):
    n=len(d)
    for i in d:
        if i%2:
            return False
    return True
n=int(input())
d=list(map(int,input().split()))
res=even_array(d)
print(res)