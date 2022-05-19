def vowels(d,k):
    for i in range(len(d)):
        if d[i]==k:
            print('True')
            return i
    return False

n=input()
v=input()
d=list(n)
r=vowels(d,v)
print(r)
