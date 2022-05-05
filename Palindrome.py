n=int(input())
temp=n
rev=0
while n:
    d=n%10
    n=n//10
    rev=rev*10+d
if rev==temp:
    print("True")
else:
    print("False")