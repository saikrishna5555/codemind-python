n=int(input())
for i in range(0,100):
    b=bin(i).replace('0b','')
    l=len(b)
    if len(b)<=n:
        r=n-l
        a='0'*r
        b=b[::-1]
        b+=a
        b=b[::-1]
        print(b)