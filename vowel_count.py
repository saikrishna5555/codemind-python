def vowels(d):
    v='aeiouAEIOU'
    c=0
    for i in d:
        if i in v:
            c+=1
    if c==0:
        return 0
    return c
    
n=input()
d=list(n)
r=vowels(d)
print(r)