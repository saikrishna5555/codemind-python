n=int(input())
st=list(map(int,input().split()))
s=int(input())
et=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(n):
    if st[i]<=qt<=et[i]:
        c+=1
print(c)