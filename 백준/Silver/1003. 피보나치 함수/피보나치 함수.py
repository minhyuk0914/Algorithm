import sys

T = int(sys.stdin.readline())

cases = []
for _ in range(T):
    cases.append(int(sys.stdin.readline()))

# dp = [[0, 0]] * (40 + 1) X 
# -> 가변 객체를 담을 경우 같은 객체를 참조하므로,
# 한 요소를 변경하면 다른 요소들도 함께 변경된다.
# 따라서 가변 객체를 다루는 2차원 부터는 for 문으로 생성
dp = [[0, 0] for _ in range(40 + 1)]

for i in range(0, max(cases) + 1):
    if i == 0:
        dp[i] = [1, 0]
    elif i == 1:
        dp[i] = [0, 1]
    else:
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0]  # 0 호출 횟수
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1]  # 1 호출 횟수

for n in cases:
    print(dp[n][0], dp[n][1])