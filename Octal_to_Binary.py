t=int(input())
for i in range(t):
    a=int(input())
    d=0
    res=0
    i=0
    while a:
        d=a%10
        a=a//10
        res+=d*(8**i)
        i+=1
    print(bin(res).replace('0b',''))