import sys 
from itertools import permutations

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

ans = 0

for li in permutations(arr, N):
    total = 0
    for i in range(1, N):
        total += abs((li[i-1] - li[i]))

    if ans < total:
        ans = total

print(ans)
