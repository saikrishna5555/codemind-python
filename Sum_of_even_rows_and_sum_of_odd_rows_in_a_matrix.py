n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
es=0
os=0
for i in range(len(e)):
    if i%2==0:
        es+=sum(e[i])
    else:
        os+=sum(e[i])
print(es,os)