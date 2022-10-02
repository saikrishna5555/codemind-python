n=int(input())
d=list(map(int,input().split()))
m=int(input())
a=list(map(int,input().split()))
sd=sorted(d)
sa=sorted(a)
if sd==sa:
    print("True")
else:
    print("False")