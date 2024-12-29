import sys

N = int(sys.stdin.readline())

stairs = [0] # index 맞추기 위함
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

dp = [0] * (N + 1)

# i번째 계단의 최대 점수는 
# max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i]

for i in range(1, N + 1):
    if i == 1:
        dp[i] = stairs[i]
    elif i == 2:
        dp[i] = dp[i - 1] + stairs[i]
    else:
        dp[i] = max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i] 
print(dp[N])