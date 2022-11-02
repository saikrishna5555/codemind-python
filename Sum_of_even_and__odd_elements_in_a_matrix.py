n,m=map(int,input().split())
e=[]
for i in range(n):
    d=list(map(int,input().split()))
    e.append(d)
es=0
os=0
for i in e:
    for j in range(len(i)):
        if i[j]%2==0:
            es+=i[j]
        else:
            os+=i[j]
print(es,os)
