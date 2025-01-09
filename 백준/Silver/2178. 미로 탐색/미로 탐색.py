from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

li = []
for _ in range(N):
    li.append(list(map(str, sys.stdin.readline().strip())))

visit = [[False] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
queue = deque([(0, 0)])
visit[0][0] = True
dist[0][0] = 0

while len(queue) != 0:
    row, col = queue.popleft()

    if row > 0 and li[row - 1][col] == '1' and not visit[row - 1][col]:
        queue.append((row - 1, col))
        visit[row - 1][col] = True
        dist[row - 1][col] = dist[row][col] + 1

    if row < N - 1 and li[row + 1][col] == '1' and not visit[row + 1][col]:
        queue.append((row + 1, col))
        visit[row + 1][col] = True
        dist[row + 1][col] = dist[row][col] + 1

    if col > 0 and li[row][col - 1] == '1' and not visit[row][col - 1]:
        queue.append((row, col - 1))
        visit[row][col - 1] = True
        dist[row][col - 1] = dist[row][col] + 1

    if col < M - 1 and li[row][col + 1] == '1' and not visit[row][col + 1]:
        queue.append((row, col + 1))
        visit[row][col + 1] = True
        dist[row][col + 1] = dist[row][col] + 1

# 이동거리 + 첫 번째 칸(1)
print(dist[N - 1][M - 1] + 1)