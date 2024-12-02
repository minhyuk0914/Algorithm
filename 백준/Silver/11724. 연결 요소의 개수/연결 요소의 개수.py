import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


graph = { i :[] for i in range(N + 1) }



for i in range(M):
    u, v = map(int, sys.stdin.readline().split())

    # 양방향 그래프
    graph[u].append(v)
    graph[v].append(u)


visit = [False] * (N + 1)

ans = 0

for i in range(1, N + 1):
    if visit[i]:
        continue

    # BFS 시작
    ans += 1

    queue = deque([i])
    visit[i] = True

    while len(queue) != 0:
        u = queue.popleft()

        for v in graph[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True

print(ans)