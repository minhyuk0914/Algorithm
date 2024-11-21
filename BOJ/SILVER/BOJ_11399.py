import sys

N = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

li.sort()


""" 
ans_li를 초기화 후 이전 값 + li의 새로운 값을 더하면서,
ans_li를 추가하는 방식
"""

ans_li = [0] * N
ans_li[0] = li[0]


for i in range(1, N):
    ans_li[i] = ans_li[i-1] + li[i]

# print(ans_li) # [1, 3, 6, 9, 13]
print(sum(ans_li))


# """ 
# ans_li를 초기화 후 이전 값 + li의 새로운 값을 더하면서,
# ans_li를 추가하는 방식(append()활용)
# """

# ans_li = [li[0]]

# for i in range(1, N):
#     ans_li.append(li[i] + ans_li[i-1])

# print(ans_li) # [1, 3, 6, 9, 13]
# print(sum(ans_li))



# """
# sum을 반복 호출
# """

# ans_li = []
# for i in range(N):
#     ans_li.append(sum((li[0:(i+1)])))

# # print(ans_li) # [1, 3, 6, 9, 13]
# print(sum(ans_li))