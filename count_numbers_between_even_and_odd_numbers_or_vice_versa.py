n=int(input())
d=list(map(int,input().split()))
l=len(d)
c=0
for i in range(0,l):
    if i>l-2:
        break
    if i>0:
        if d[(i-1)]%2==0 and d[(i+1)]%2!=0:
            c+=1
        elif d[(i-1)]%2!=0 and d[(i+1)]%2==0:
            c+=1
print(c)