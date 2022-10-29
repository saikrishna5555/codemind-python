s=input()
n='0123456789'
s=list(s)
s.insert(0,'.')
s=''.join(s)
summ=0
for i in range(1,len(s)):
    if s[i] in n:
        if s[i-1]=='+':
            summ+=int(s[i])
        elif s[i-1]=='-':
            summ-=int(s[i])
        else:
            summ+=int(s[i])
print(summ)