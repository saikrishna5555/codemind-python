n=int(input())
d=list(map(int,input().split()))
dic={}
for i in d:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
m=max(dic.values())
for k,v in dic.items():
    if v==m:
        print(k)
        break