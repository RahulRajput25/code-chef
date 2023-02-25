t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x*2 < y*5:
        print("candy")
    elif x*2 == y*5:  
        print("either")
    else:
        print("chocolate")
