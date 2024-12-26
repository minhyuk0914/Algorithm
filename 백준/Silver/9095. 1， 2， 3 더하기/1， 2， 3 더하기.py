import sys

T = int(sys.stdin.readline())

case = []
for i in range(T):
    case.append(int(sys.stdin.readline()))

# N-1 에서 1 더하기 -> N-1 을 만드는 경우의 수와 동일 == dp[N-1]
# N-2 에서 2 더하기 -> N-2 을 만드는 경우의 수와 동일 == dp[N-2]
# N-3 에서 3 더하기 -> N-3 을 만드는 경우의 수와 동일 == dp[N-3]

dp = [0] * (max(case) + 1)

for i in range(1, max(case) + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

for n in case:
    print(dp[n])