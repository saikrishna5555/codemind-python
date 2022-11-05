s=input()
s=s.split()
mis=0
mxs=0
for i in s:
    mis+=ord(min(i))
    mxs+=ord(max(i))
print(abs(mis-mxs))