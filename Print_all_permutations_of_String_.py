from itertools import permutations
n=input()
a=list(permutations(n))
for i in a:
    i=''.join(i)
    print(i)