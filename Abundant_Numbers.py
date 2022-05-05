n=int(input())
facsum=0
for i in range(1,n):
    if n%i==0:
        facsum+=i
if n<facsum:
    print("True")
else:
    print("False")