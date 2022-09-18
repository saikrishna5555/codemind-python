n=int(input())
a=0
for i in range(1,n):
    if n%i==0:
        a+=i
if n==a:
    print("True")
else:
    print("False")