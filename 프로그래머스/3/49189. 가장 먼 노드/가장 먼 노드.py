from collections import deque

def solution(n, edge):
    answer = 0
    route = [0] * (n + 1)
    graph = [[] for i in range(n + 1)]
    q = deque()
    
    #무방향 그래프
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 1번 노드에서 가장 멀리 떨어진 노드의 갯수 확인 문제
    q.append(1)
    route[1] = 1
    
    while q:
        now = q.popleft()
        for g in graph[now]:
            if route[g] == 0:
                q.append(g)
                route[g] = route[now] + 1
                
    # print(route) # [0, 1, 2, 2, 3, 3, 3]
    
    # 가장 먼 노드의 개수 확인
    max_edge = max(route)
    
    for i in route:
        if i == max_edge:
            answer += 1
            
    return answer