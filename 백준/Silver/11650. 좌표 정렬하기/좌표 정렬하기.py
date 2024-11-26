import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
    x_y = list(map(int, sys.stdin.readline().split()))
    li.append(x_y)

li.sort()

for ans in li:
    print(*ans)