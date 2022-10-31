s=input()
a="@#£_&+-()/?!+:'*~`|•√π÷×¶∆\}{==°^¢$¥€%©®™✓[]>><,."
c=0
for i in s:
    if i in a:
        c+=1
print(c)