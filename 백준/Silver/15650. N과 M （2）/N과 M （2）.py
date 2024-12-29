import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

num_li = [x for x in range(1, N + 1)]
for li in combinations(num_li, M):
    print(*li)