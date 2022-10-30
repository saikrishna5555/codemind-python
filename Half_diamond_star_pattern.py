n=int(input())
if n<3:
    print("The pattern is not possible")
else:
    for i in range(1,n+1):
        print('*'*i)
    for j in range(1,n):
        print('*'*(n-j))
        