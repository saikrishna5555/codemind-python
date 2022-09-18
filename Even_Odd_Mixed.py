n=int(input())
e=0
o=0
while n:
    d=n%10
    n=n//10
    if d%2==0:
        e+=1
    else:
        o+=1
if e!=0 and o!=0:
    print("Mixed")
elif e==0 and o!=0:
    print("Odd")
else:
    print("Even")