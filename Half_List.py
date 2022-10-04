n=int(input())
d=list(map(int,input().split()))
m=n//2
a=d[0:m]
b=d[m:]
b=b[::-1]
print(*(b+a))