def solution(n, computers):
    visited = [False] * n

    def dfs(node):
        # 현재 노드를 방문 처리
        visited[node] = True
        
        # 현재 노드와 연결된 다른 노드 탐색
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    answer = 0

    # 모든 컴퓨터를 순회
    for i in range(n):
        # 방문하지 않은 컴퓨터를 찾으면 새로운 네트워크 발견
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer