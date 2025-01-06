import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

# 상근이(1)의 친구
friend = [0] * (N + 1)

# 상근이의 학번이 1이므로 graph 1의 해당하는 친구를 체크
for i in graph[1]:
    friend[i] = 1

# 상근이(1)의 친구의 친구
friend_2 = [0] * (N + 1)

# 이미 상근이(1)과 친구인 사람들은 제외
for i in range(1, N + 1):
    if friend[i] == 0:  # 상근이(1)의 친구가 아니면 스킵
        continue
    
    # 상근이(1)의 친구인 사람(i)의 친구들을 탐색
    for j in graph[i]:
        if j != 1 and friend[j] == 0: # 상근이 자신이 아니고, 상근이와 직접 친구가 아닌 경우
            friend_2[j] = 1

print(sum(friend) + sum(friend_2))