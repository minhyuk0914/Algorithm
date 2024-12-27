import sys

N = int(sys.stdin.readline())

# DP 배열 초기화
dp = [-1] * (N + 1)

# 기본값 설정 (3kg과 5kg 봉지로 정확히 나눌 수 있는 경우)
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

# DP 배열 계산
for i in range(6, N + 1):
    if dp[i - 3] != -1:  # 3kg 봉지를 추가로 사용 가능한 경우
        dp[i] = dp[i - 3] + 1
    if dp[i - 5] != -1:  # 5kg 봉지를 추가로 사용 가능한 경우
        if dp[i] == -1:  # 아직 dp[i]가 갱신되지 않은 경우
            dp[i] = dp[i - 5] + 1
        else:  # dp[i]가 이미 갱신된 경우, 최소값 선택
            dp[i] = min(dp[i], dp[i - 5] + 1)

print(dp[N])