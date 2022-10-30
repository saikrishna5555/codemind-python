t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    for i in s:
        if s.count(i)==1:
            a=i
            break
        else:
            c+=1
    if c==len(s):
        print(-1)
    else:
        print(a)