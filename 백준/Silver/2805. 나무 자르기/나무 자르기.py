import sys

N, M = map(int, sys.stdin.readline().split())

trees = list(map(int, sys.stdin.readline().split()))
trees.sort()
low, high = 1, trees[-1]

ans = 0
while low <= high:
    mid = (low + high) // 2

    total = 0

    for tree in trees:
        if tree > mid:
            total += tree - mid

    if total >= M:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)