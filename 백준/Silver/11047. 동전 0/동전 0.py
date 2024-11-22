import sys

N, K = map(int, sys.stdin.readline().split())

sorted_li = []
ans = 0

for i in range(N):
    sorted_li.append(int(sys.stdin.readline()))

for idx in range(len(sorted_li)-1, -1, -1):
    if sorted_li[idx] > K:
        pass
    else:
        ans += K // sorted_li[idx]
        K %= sorted_li[idx]
print(ans)