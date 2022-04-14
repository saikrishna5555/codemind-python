n=int(input())
i=0
while True:
    a=i
    b=i+1
    c=a*b
    i+=1
    if c==n:
        print("YES")
        break
    if c>=n:
        print("NO")
        break
    
    