# cook your dish here
T = int(input())
for i in range(T):
    X, Y = list(map(int, input().split()))
    print("YES" if X >= Y else "NO")
