s=input()
s=list(s)
v='aeiouAEIOU'
i=0
j=len(s)-1
while j>=i:
    if s[i] in v and s[j] in v:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    elif s[i] in v and s[j] not in v:
        j-=1
    elif s[i] not in v and s[j] in v:
        i+=1
    else:
        i+=1
        j-=1
print(''.join(s))