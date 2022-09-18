t=int(input())
for i in range(t):
    n=int(input())
    t=n
    rev=0
    while n:
        d=n%10
        rev=rev*10+d
        n=n//10
    if t==rev:
        print("True")
    else:
        print("False")