import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(int(sys.stdin.readline()))

# 리스트 정렬
li.sort()

# 가장 작은 수 * N 를 반복적으로 하면서,
# 최대로 가질 수 있는 중량을 ans_li에 저장
ans_li = [] 
for x in li:
    ans_li.append(x * N)
    N -= 1

# print(ans_li)   # [20, 15]
print(max(ans_li))