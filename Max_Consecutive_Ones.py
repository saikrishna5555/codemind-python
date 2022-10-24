n=int(input())
d=list(map(int,input().split()))
j=0
i=0
m=0
while n!=j:
    if d[j]==1:
        m=max(m,j-i+1)
        j+=1
    else:
        j+=1
        i=j
print(m)