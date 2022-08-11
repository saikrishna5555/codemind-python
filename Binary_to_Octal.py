t=int(input())
for i in range(t):
    a=int(input())
    i=0
    d=0
    res=0
    while a:
        d=a%10
        a=a//10
        res+=d*(2**i)
        i+=1
    print(oct(res).replace('0o',''))