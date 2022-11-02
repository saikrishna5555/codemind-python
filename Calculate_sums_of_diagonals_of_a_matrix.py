n=int(input())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
d=0
sd=0
k=n-1
for i in range(n):
    d+=e[i][i]
    sd+=e[i][k]
    k-=1
print('Principal Diagonal:{}' .format(d))
print('Secondary Diagonal:{}' .format(sd))