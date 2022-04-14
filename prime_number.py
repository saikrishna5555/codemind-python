num=int(input())
for i in range(2,num):
    if num%i==0:
        print("not a prime")
        break
else:
    print("prime")
    