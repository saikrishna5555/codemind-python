h,s,p=map(int,input().split())
if h>50 and s>60 and p>100:
    print(10)
elif s>60 and p>100:
    print(8)
elif h>50 and s>60:
    print(9)
elif h>50 and p>100:
    print(7)
elif h>50 or s>60 or p>100:
    print(6)
else:
    print(5)