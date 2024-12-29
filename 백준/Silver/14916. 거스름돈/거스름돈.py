import sys 

N = int(sys.stdin.readline())

dp = [-1] * (N + 1)

if N >= 2:
    dp[2] = 1
if N >= 4:
    dp[4] = 2
if N >= 5:
    dp[5] = 1

# DP 계산
for i in range(6, N + 1):
    if dp[i - 2] != -1:  # 2원을 추가할 수 있는 경우
            dp[i] = dp[i - 2] + 1
    if dp[i - 5] != -1:  # 5원을 추가할 수 있는 경우
        if dp[i] == -1:  # 아직 갱신되지 않은 경우
            dp[i] = dp[i - 5] + 1
        else:  # 이미 값이 있는 경우 최소값 선택
            dp[i] = min(dp[i], dp[i - 5] + 1)
print(dp[N])
