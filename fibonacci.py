def fib_seq(n):
    a,b=0,1
    print(a,b,end=' ')
    for i in range(3,n+1):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input())
fib_seq(n)