import sys
from collections import Counter


N, C = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))  # 모든 입력을 정수로 변환

counter = Counter(li)

# print(counter.most_common()) # [(1, 3), (3, 3), (2, 3)]

answer = []
for key, val in counter.most_common():
    answer += [key] * val

print(*answer)