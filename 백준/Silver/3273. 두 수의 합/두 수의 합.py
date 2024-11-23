from itertools import combinations
import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())

# 리스트 정렬
li.sort()

start_idx = 0
end_idx = N - 1
ans = 0

while start_idx < end_idx:
    # 시작점 값과 끝점 값의 합이 X 인경우
    if li[start_idx] + li[end_idx] == X:
        ans += 1
        start_idx += 1
    # 시작점 값과 끝점 값의 합이 X 보다 작은 경우
    elif li[start_idx] + li[end_idx] < X:
        start_idx += 1
    # 시작점 값과 끝점 값의 합이 X 보다 큰 경우
    else:
        end_idx -= 1

print(ans)



# # 메모리 초과(조합 활용)
# ans = 0
# for i in list(combinations(li, 2)):
#     if sum(i) == 13:
#         ans += 1

# print(ans)