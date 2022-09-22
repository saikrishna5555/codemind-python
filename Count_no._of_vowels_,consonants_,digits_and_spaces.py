s=input()
v='aeiou'
dd='1234567890'
w=' '
vc=0
cc=0
d=0
wc=0
for i in s:
    i=i.lower()
    if i in v:
        vc+=1
    elif i in dd:
        d+=1
    elif i==' ':
        wc+=1
    else:
        cc+=1
print("Vowels:",vc)
print("Consonants:",cc)
print("Digits:",d)
print('White spaces:',wc)