s=input()
f=s[0:2]
l=s[2:]
t=int(f)
if t>12:
    t=t-12
    t=str(t)
    if len(t)==1:
        t='0'+t
    i=' PM'
elif t==0:
    t=t+12
    t=str(t)
    i=" AM"
elif t==12:
    t=str(t)
    i=' PM'
else:
    t=f
    i=' AM'
print(t+l+i)
    