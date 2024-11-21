import sys
from itertools import combinations

li = []
ans = ""

for i in range(9):
    height = int(sys.stdin.readline())
    li.append(height)

per_7 = list(combinations(li, 7))

for i in range(len(per_7)):
    if sum(per_7[i]) == 100:
        ans = sorted(list(per_7[i]))
        # for x in ans:
        #     print(x)
        break

print(*ans, sep = '\n')