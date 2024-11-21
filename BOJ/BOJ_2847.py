import sys

N = int(sys.stdin.readline())

scores = []

for i in range(N):
    scores.append(int(sys.stdin.readline()))

cnt = 0
for i in range(N-1, 0, -1):
    if scores[i] <= scores[i - 1]:
        cnt += scores[i-1] - scores[i] + 1
        scores[i-1] = scores[i] - 1
print(cnt)