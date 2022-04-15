n=int(input())
big=0
while n:
    d=n%10
    if big<d:
        big=d
    n=n//10
print(big)
    