import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

find_s = 'IOI' + 'OI' * (N-1)

ans = 0
for i in range(M):
    if S[i : i + len(find_s)] == find_s:
        ans += 1

print(ans)