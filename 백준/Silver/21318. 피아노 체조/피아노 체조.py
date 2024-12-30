import sys

N = int(sys.stdin.readline())
li = [0] + list(map(int, sys.stdin.readline().split()))

# 실수 여부 판단 리스트 생성
mistake = [0] * N  # 0부터 시작, 길이는 N
for i in range(1, N):  # 인접한 요소 비교
    if li[i] > li[i + 1]:
        mistake[i] = 1

# 누적합 계산
s_num = [0] * (N + 1)
for i in range(1, len(mistake)):
    if i == 1:
        s_num[i] = mistake[i]
    else:
        s_num[i] = mistake[i] + s_num[i - 1]


# 질문 (Q) 처리 
Q = int(sys.stdin.readline())
for _ in range(Q):
    x, y = map(int, sys.stdin.readline().split())

    if x == y: # 같은 위치의 경우, 항상 0 출력
        print(0)
        continue

    else:
        ans = s_num[y - 1] - s_num[x - 1]
        print(ans)
