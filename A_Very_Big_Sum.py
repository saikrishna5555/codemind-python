def aVeryBigSum(d):
    return sum(d)

n=int(input())
d=list(map(int,input().split()))
s=aVeryBigSum(d)
print(s)