s=input()
f=s[0:2]
m=s[2:5]
l=s[6:]
t=int(f)
if t==12 and l=='AM':
    t='00'
elif t==12 and l=="PM":
    t=f
elif l=="PM":
    t=t+12
    t=str(t)
    if len(t)==1:
        t='0'+t
else:
    t=f
print(t+m)