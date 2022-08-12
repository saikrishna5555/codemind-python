n = int(input())
for i in range(n):
    a=input()
    for j in a:
        r=int(a,16)
        r=bin(r).replace('0b','')
        while len(r)%4!=0:
            r='0'+r
    print(r)