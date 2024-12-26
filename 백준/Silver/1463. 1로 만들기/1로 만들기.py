import sys

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
dp[1] = 0

for i in range(2, N + 1):
    # 이전 index의 값 + 1(1을 뺀다는 규칙)으로 저장
    dp[i] = 1 + dp[i - 1]

    # 3으로 나누어 떨어지면 3으로 나누고, dp[i] 중 최솟값으로 저장
    if i % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 3])

    # 2으로 나누어 떨어지면 2으로 나누고, dp[i] 중 최솟값으로 저장
    if i % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 2])

print(dp[N])