def palin(s):
    if s==s[::-1]:
        return True
    return False
t=int(input())
for i in range(t):
    s=input()
    if palin(s):
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")