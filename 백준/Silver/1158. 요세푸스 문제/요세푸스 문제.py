import sys

N, K = map(int, sys.stdin.readline().split())

num_li = [x for x in range(1, N + 1)]
ans = []
idx = K - 1
while num_li:
    idx = idx % len(num_li)
    ans.append(num_li.pop(idx))
    idx += K - 1

print(f"<{', '.join(map(str, ans))}>")