t=int(input())
e=[]
for i in range(t):
    n=input()
    e.append(n)
c=0
for i in e:
    if i=="++X" or i=="X++":
        c+=1
    else:
        c-=1
print(c)