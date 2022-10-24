def hcf(a,b):
    m=min(a,b)
    for i in range(1,m+1):
        if a%i==0 and b%i==0:
            hcf=i
    return hcf
            

n=int(input())
d=list(map(int,input().split()))
a=d[0]
b=d[1]
h=hcf(a,b)
for i in range(2,n):
    h=hcf(h,d[i])
print(h)
    