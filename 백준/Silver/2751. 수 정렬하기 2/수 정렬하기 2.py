import sys

N = int(sys.stdin.readline())

ans = []
for i in range(N):
    ans.append(int(sys.stdin.readline()))

ans.sort()

print(*ans, sep = '\n')