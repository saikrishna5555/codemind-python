def rev(n):
    a=n[::-1]
    return a

n=input()
s=n.split()
re=rev(s)
print(*re)