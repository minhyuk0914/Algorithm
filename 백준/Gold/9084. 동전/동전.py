import sys

T = int(sys.stdin.readline())

for _ in range(T):

    N = int(sys.stdin.readline())

    li = list(map(int, sys.stdin.readline().split()))
    
    M = int(sys.stdin.readline())

    dp = [0] * (M + 1)
    dp[0] = 1

    for i in li:
        for j in range(i, M + 1):
            dp[j] += dp[j - i]
    print(dp[M])