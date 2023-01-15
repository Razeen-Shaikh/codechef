# cook your dish here
N = int(input())
for i in range(N):
    A = list(map(int, input().split()))
    A = sorted(A)
    print(A[1])
