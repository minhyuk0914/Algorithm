import sys

N = int(sys.stdin.readline())

li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()

ans = 0

for idx in range(len(li)):
    ans += abs(idx + 1 - li[idx])

print(ans)