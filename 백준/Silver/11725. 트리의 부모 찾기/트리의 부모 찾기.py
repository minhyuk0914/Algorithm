import sys

# 런타임 에러 / BOJ에서는 재귀함수가 1000으로 지정되어 있어서 늘리기 위함
sys.setrecursionlimit(10**6)


N = int(sys.stdin.readline())
visited = [0] * (N + 1)
tree = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

for _ in range(1, N):
    n1, n2 = map(int, sys.stdin.readline().split())

    # 인접 리스트 저장 
    tree[n1].append(n2)
    tree[n2].append(n1)

# DFS
def DFS(x):
    visited[x] = 1
    for i in tree[x]:
        if not visited[i]:
            answer[i] = x
            DFS(i)

# 루트노드 1부터 실행
DFS(1)

# print(answer) # [0, 0, 4, 6, 1, 3, 1, 4]

# 2번째 노드부터 출력
for i in range(2, N+1):
    print(answer[i])