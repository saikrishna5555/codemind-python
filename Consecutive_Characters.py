s=input()
a=0
i=0
j=0
while j<len(s):
    if s[j]==s[i]:
        a=max(a,j-i+1)
        j+=1
    else:
        i=j
print(a)