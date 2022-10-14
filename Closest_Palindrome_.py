def palin(n):
    t=n
    r=0
    while n:
        d=n%10
        r=r*10+d
        n=n//10
    if t==r:
        return True
    return False
n=int(input())
a=n-1
b=n+1
ad=0
bd=0
while True:
    if palin(a) and palin(b):
        if ad==bd:
            print(a,b)
            break
        elif ad<bd:
            print(a)
            break
        else:
            print(b)
            break
    elif palin(a):
        print(a)
        break
    elif palin(b):
        print(b)
        break
    
    else:
        a-=1
        b+=1
        ad+=1
        bd+=1