n=int(input())
d=list(map(int,input().split()))
s=sum(d)
if s%4==0:
    print('X')
else:
    print("Y")