def rev(n):
    a=n[::-1]
    return a

n=input()
s=n.split()
for i in range(0,len(s)):
    if i%2==0:
        s[i]=rev(s[i])
print(*s)