import sys
from collections import deque

N = int(sys.stdin.readline()) # 정점(Vertex)(노드) 수
M = int(sys.stdin.readline()) # 입력 그래프 쌍 수

graph = { i :[] for i in range(N + 1) }
# print(graph) # {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}


for i in range(M):
    vertex_1, vertex_2 = map(int, sys.stdin.readline().split())

    # 양방향 그래프
    graph[vertex_1].append(vertex_2)
    graph[vertex_2].append(vertex_1)

# print(graph) # {0: [], 1: [2, 5], 2: [1, 3, 5], 3: [2], 4: [7], 5: [1, 2, 6], 6: [5], 7: [4]}

visited = [False] * (N + 1)
ans = 0

# BFS : 너비 우선 탐색 (1 - 2 - 5 - 3 - 6)
def BFS(x):
    que = deque()
    global ans
    que.append(x)
    visited[x] = True

    while que:
        n = que.popleft()
        for n_next in graph[n]:
            if not visited[n_next]:
                visited[n_next] = True
                que.append(n_next)
                ans += 1

BFS(1) # 1번에서 BFS 실행
# print(visited) [False, True, True, True, False, True, True, False]
print(ans)