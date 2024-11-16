import sys

N = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

low, high = 0, max(n_list)
answer = 0

while low <= high:
    total_sum = 0
    mid = (low + high) // 2

    for i in range(N):
        total_sum += min(mid, n_list[i])

    if total_sum <= M:  # 예산(M) 내에서 가능한 경우
        answer = mid
        low = mid + 1

    else:               # 예산(M)을 초과한 경우
        high = mid - 1

print(answer)