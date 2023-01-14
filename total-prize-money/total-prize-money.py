# cook your dish here
T = int(input())
for i in range(T):
    X, Y = list(map(int, input().split()))
    X, Y = max(X, Y), min(X, Y)
    print(X * 10 + Y * 90)
