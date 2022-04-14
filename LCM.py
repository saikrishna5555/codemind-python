a,b=map(int,input().split())
big=max(a,b)
small=min(a,b)
i=1
c=big
while True:
    if big%small==0:
        print(big)
        break
    else:
        big=c*i
        i+=1