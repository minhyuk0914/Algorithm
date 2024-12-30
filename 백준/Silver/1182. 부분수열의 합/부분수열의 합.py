import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in range(1, N + 1):
    for comb in combinations(li, i):
        if sum(comb) == S:
            ans += 1

print(ans)