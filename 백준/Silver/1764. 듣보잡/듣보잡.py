import sys

N, M = map(int, sys.stdin.readline().split())

n_group = set()
m_group = set()
for _ in range(N):
    n_group.add(sys.stdin.readline().strip())

for _ in range(M):
    m_group.add(sys.stdin.readline().strip())

ans = list(n_group & m_group)
ans.sort()

print(len(ans))
for name in ans:
    print(name)