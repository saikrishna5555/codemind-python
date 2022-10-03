m=int(input())
n=int(input())
e=[]
for i in range(m):
    arr=list(map(int,input().split()))
    s=sum(arr)
    e.append(s)
print(sum(e))