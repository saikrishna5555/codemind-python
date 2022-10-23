def lcm(a,b):
    big=max(a,b)
    small=min(a,b)
    i=2
    b=big
    while big%small:
        big=b*i
        i+=1
    return big
n=int(input())
a=list(map(int,input().split()))
f1=a[0]
f2=a[1]
lc=lcm(f1,f2)
for i in range(2,n):
    lc=lcm(lc,a[i])
print(lc)