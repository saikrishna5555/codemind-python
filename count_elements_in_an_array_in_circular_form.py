n=int(input())
d=list(map(int,input().split()))
a=d[0]
d.insert(0,d[-1])
d.append(a)
c=0
for i in range(1,len(d)-1):
    if d[i-1]%2==0 and d[i+1]%2:
        c+=1
    elif d[i-1]%2 and d[i+1]%2==0:
        c+=1
print(c)