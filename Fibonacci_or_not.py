n=int(input())
a,b=0,1

while True:
    if n==0 or n==1:
        print('True')
        break
    c=a+b
    if c==n:
        print("True")
        break
    
    
    a=b
    b=c
    if c>n:
        print("False")
        break