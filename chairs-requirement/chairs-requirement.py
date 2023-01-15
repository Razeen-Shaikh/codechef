# cook your dish here
T = int(input())
for i in range(T):
    X, Y = list(map(int, input().split()))
    print(X - Y if X - Y >= 0 else 0)
