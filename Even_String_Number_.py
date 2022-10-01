s=input()
d=[]
c=999999999
for i in s:
    if i.isnumeric():
        i=int(i)
        if i%2==0:
            d.append(str(i))
            if i<c:
                c=i
        else:
            d.append(str(i))
d=set(d)
d=sorted(d)
if c==999999999:
    print(-1)
else:
    d.remove(str(c))
    d=d[::-1]
    d=''.join(d)
    d+=str(c)
    print(d)