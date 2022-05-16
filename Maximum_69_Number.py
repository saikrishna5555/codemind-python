n=int(input())
d=list(str(n))
for i in range(0,len(d)):
    if d[i]=='6':
        d[i]=str(9)
        break
print(''.join(d))