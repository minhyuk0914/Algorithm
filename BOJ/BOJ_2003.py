import sys

N, M = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))

ans = 0
start = 0
end = 0
total_sum = li[0] # 첫번째 인덱스 부터 시작

while True:
    if total_sum == M:  # 현재 구간의 합 체크
        ans += 1
    if total_sum >= M:  # sum이 M보다 큰 경우
        start += 1
        total_sum -= li[start - 1]
    else:   # sum이 M보다 작은 경우
        if end == N - 1:
            break
        
        end += 1
        total_sum += li[end]

print(ans)