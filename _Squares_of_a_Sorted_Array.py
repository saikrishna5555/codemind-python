n=int(input())
d=list(map(int,input().split()))
e=[]
for i in d:
    e.append(i*i)
print(*sorted(e))