def adam_no(n):
    rev=0
    while n:
        d=n%10
        n=n//10
        rev=rev*10+d
    return rev
n=int(input())
sq=n**2
rev_num=adam_no(n)
rev_num_sq=rev_num**2
if sq==adam_no(rev_num_sq):
    print("True")
else:
    print("False")