t=int(input())
for i in range(t):
    x=int(input())
    if x<3:
        print("light")
    elif x>=3 and x<7:
        print("moderate")
    else:
        print("heavy")