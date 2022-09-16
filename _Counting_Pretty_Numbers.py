t=int(input())
for i in range(t):
    l,r=map(int,input().split())
    c=0
    for k in range(l,r+1):
        a=k%10
        if a==2 or a==3 or a==9:
            c+=1
    print(c)