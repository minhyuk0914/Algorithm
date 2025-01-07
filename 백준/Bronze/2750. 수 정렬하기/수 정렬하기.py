import sys

N = int(sys.stdin.readline())

li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))

li.sort()

for ans in li:
    print(ans)