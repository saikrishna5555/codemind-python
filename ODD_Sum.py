def odd_sum(d):
    n=len(d)
    os=0
    for i in d:
        if i%2:
            os+=i
    return os    

n=int(input())
d=list(map(int,input().split()))
os=odd_sum(d)
print(os)

