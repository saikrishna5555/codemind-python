def vowels(d,d1):
    a=[]
    c=0
    for i in d:
        if i not in d1:
            a+=[i]
            c+=1
    a=' '.join(a)
    if c==0:
        return 0
    else:
        
        return a

n=input()
v='aeiou'
d1=list(n)
d=list(v)
res=vowels(d,d1)
print(res)