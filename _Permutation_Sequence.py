from itertools import permutations
n,m=map(int,input().split())
s=''
for i in range(1,n+1):
    i=str(i)
    s+=i
r=list(permutations(s,n))[m-1]
print(''.join(r))