import sys

N, M = map(int, sys.stdin.readline().split())

li = [0]
name_dict = {}
for i in range(1, N + 1):
    name = sys.stdin.readline().strip()
    li.append(name)
    name_dict[name] = i

for _ in range(M):
    q = sys.stdin.readline().strip()

    if q.isdigit():
        print(li[int(q)])
    else:
        print(name_dict[q])