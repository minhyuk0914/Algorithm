import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0] * (K + 1)
items = []
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().split())))


for W, V in items:
    # 역순으로 계산
    for i in range(K, W - 1, -1):
        dp[i] = max(dp[i], dp[i-W] + V)
        
print(dp[K])