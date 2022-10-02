n=int(input())
nums=list(map(int,input().split()))
m=int(input())
ind=list(map(int,input().split()))
t=[]
for i in range(n):
    t.insert(ind[i],nums[i])
print(*t)