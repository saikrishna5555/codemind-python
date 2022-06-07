s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
d=sorted(s1)
d1=sorted(s2)
d=''.join(d)
d1=''.join(d1)
if d==d1:
    print("True")
else:
    print("False")