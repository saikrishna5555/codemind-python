s=input()
v='aeiouAEIOU'
s=s.split()
e=[]
c=1
for i in s:
    a=i[0]
    if a in v:
        i=i+'ma'+'a'*c
        e.append(i)
        c+=1
    else:
        i=i.replace(a,'')
        i+=a+'ma'+'a'*c
        e.append(i)
        c+=1
        
        
print(*e)