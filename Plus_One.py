n=int(input())
d=list(map(int,input().split()))
s=''
for i in d:
    i=str(i)
    s+=i
s=int(s)+1
s=str(s)
e=[]
for i in s:
    i=int(i)
    e.append(i)
print(*e)