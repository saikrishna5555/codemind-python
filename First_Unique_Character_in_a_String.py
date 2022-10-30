s=input()
c=0
for i in range(len(s)):
    if s.count(s[i])==1:
        print(i)
        break
    else:
        c+=1
if c==len(s):
    print(-1)