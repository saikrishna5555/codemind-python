N,M =map(int,input().split())
t=2
lcm=1
while True:
    if N%t==0 and M%t==0:
        N=N//t
        M=M//t
        lcm=lcm*t
    else:
        t+=1
    if N<t or M<t:
        break
print(lcm)