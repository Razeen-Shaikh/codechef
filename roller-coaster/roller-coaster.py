# cook your dish here
T = int(input())
for i in range(T):
    X, H = list(map(int, input().split()))
    if X >= H:
        print("YES")
    else:
        print("NO")
