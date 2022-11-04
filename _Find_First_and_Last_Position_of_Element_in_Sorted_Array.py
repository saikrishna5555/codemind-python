n=int(input())
d=list(map(int,input().split()))
t=int(input())
i=0
j=0
c=0
while j!=n:
    if d[j]==t:
        if i==0:
            i=j
            c=1
            j+=1
        else:
            j+=1
    else:
        if c==1:
            break
        else:
            j+=1
        
if i==0 and j==n:
    print(-1,-1)
else:
    print(i,j-1)