s=input()
d='1234567890'
summ=0
for i in range(len(s)):
    if s[i] in d:
        summ+=int(s[i])
print(summ)