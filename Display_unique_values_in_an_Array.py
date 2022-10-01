n=int(input())
d=list(map(int,input().split()))
dic={}
for i in d:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
e=[]
for k,v in dic.items():
    if v==1:
        e.append(k)
if len(e)==0:
    print(-1)
else:
    print(*sorted(e))