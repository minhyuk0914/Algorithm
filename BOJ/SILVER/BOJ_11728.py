import sys

N, M = map(int, sys.stdin.readline().split())

a_arr = list(map(int, sys.stdin.readline().split()))
b_arr = list(map(int, sys.stdin.readline().split()))

ans_arr = a_arr + b_arr
ans_arr.sort()

print(*ans_arr)
# print(" ".join(map(str, ans_arr)))