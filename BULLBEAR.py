t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("loss")
    elif x==y:
        print("neutral")
    else:
        print("profit")