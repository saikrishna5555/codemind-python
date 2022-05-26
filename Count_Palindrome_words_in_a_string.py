def rev(n):
    if n==n[::-1]:
        return True
    return False


n=input()
n=n.upper()
n=n.split()
d=list(n)
c=0
for i in d:
    if rev(i):
        c+=1
print(c)