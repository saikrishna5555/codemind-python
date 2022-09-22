s=input()
c=0
for i in s:
    if i.isnumeric():
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(c))