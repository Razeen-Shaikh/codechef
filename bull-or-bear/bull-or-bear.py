# cook your dish here
T = int(input())
for i in range(T):
    X, Y = list(map(int, input().split()))
    if (X < Y):
        print("PROFIT")
    else:
        print("LOSS" if X > Y else "NEUTRAL")
