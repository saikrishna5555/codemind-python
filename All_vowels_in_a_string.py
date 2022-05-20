n=input()
d=list(n)
v='aeiou'
d1=list(v)
c=0
for i in d1:
    if i not in d:
        print("False")
        break
    else:
        c+=1
if c==len(d1):
    print("True")