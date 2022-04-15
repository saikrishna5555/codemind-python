n=int(input())
div=n
s=0
while n:
    d=n%10
    n=n//10
    s=s+d
if div%s==0:
    print("True")
else:
    print("False")
        