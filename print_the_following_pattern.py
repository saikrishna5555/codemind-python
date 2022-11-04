n=int(input())
for i in range(n):
    a='x'*(n-1)
    a=list(a)
    a.insert(i,'0')
    print(''.join(a))