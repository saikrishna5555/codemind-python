def sq_sum(n):
    sq=0
    if n==1 or n==7:
        return True
    while n:
        d=n%10
        n=n//10
        sq+=d**2
    return sq
        
n=int(input())
res=sq_sum(n)
while n:
    if res<10:
        if res==1 or res==7:
            print("True")
            break
        else:
            print("False")
            break
    else:
        res=n
        n=sq_sum(res)