n,m=map(int,input().split())
if n%2==0 and m%2==0:
    print('Player 1')
elif n%2 and m%2:
    print("Player 2")
else:
    print("Player 1")