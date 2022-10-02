def product(d,t):
    p=1
    for i in d:
        if i==t:
            continue
        else:
            p*=i
    return p
    
n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    a=product(d,i)
    e.append(a)
print(*e)