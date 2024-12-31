import sys

N, M = map(int, sys.stdin.readline().split())

n_li = list(map(int, sys.stdin.readline().split()))

psum = [0] * (N + 1)
psum[1] = n_li[1]

# 누적 합 계산
for i in range(1, N + 1):
    if i == 1:
        psum[i] = n_li[i - 1]
    else:
        psum[i] = psum[i-1] + n_li[i - 1]

# 구간 합 구하기 
# psum[end] - psum[start - 1]
# 1 3 -> psum[3] - psum[0]
# 2 4 -> psum[4] - psum[1]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    
    ans = psum[end] - psum[start - 1] 
    print(ans)