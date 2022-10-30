s=input()
v='aeiou'
a=''
for i in s:
    if i in v:
        a+='V'
    else:
        a+='C'
r=a[0]
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        continue
    else:
        r+=a[i]
print(r)