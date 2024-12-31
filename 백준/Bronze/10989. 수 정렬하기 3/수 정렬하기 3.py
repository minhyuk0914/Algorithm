import sys

N = int(sys.stdin.readline())

li = [0] * (10000 + 1)
for _ in range(N):
    li[int(sys.stdin.readline())] += 1

for idx in range(1, 10000 + 1):
    if li[idx] != 0:
        for _ in range(li[idx]):
            print(idx)