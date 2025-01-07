import sys
from itertools import combinations
L, C = map(int, sys.stdin.readline().split())

li = list(sys.stdin.readline().split())

# 사전순으로 정렬
li.sort()

# combinations (조합) 활용
ans_li = []
for comb in combinations(li, L):
    check = 0

    # a, e, i, o, u 체크
    for x in ['a', 'e', 'i', 'o', 'u']:
        if x in comb:
            check += 1

    # a, e, i, o, u를 check 한 값이 0보다 큰 경우(최소 1)
    # 모음을 제외한 자음의 개수가 2보다 큰 경우(최소 2)
    # 최소 모음 1개 이상, 최소 자음 2개 이상
    if check >= 1 and L - check >= 2:
        ans_li.append(comb)

for ans in ans_li:
    print(''.join(ans))