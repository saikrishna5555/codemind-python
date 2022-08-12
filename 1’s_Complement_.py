n=int(input())
b=bin(n).replace('0b','')
s=''
for i in b:
    if i=='1':
        s+='0'
    else:
        s+='1'
print(int(s,2))