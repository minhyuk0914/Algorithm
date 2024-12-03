import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


graph = { i :[] for i in range(N + 1) }


for i in range(M):
    u, v = map(int, sys.stdin.readline().split())

    # 양방향 그래프
    graph[u].append(v)
    graph[v].append(u)


min_sum = 1e9
ans = -1

for i in range(1, N + 1):
    # i를 시작으로 하는 BFS
    # 각 노드까지의 최단거리를 구해서 전체 합 구하기

    visit = [False] * (N + 1)
    dist = [-1] * (N + 1)

    queue = deque([i])
    visit[i] = True
    dist[i] = 0

    while len(queue) != 0:
        u = queue.popleft()

        for v in graph[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1

    dist_sum = sum(dist)

    if min_sum > dist_sum:
        min_sum = dist_sum
        ans = i

print(ans)