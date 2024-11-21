import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split()))) # [start, end]

# li 정렬
li.sort() # key(lambda x : x[1], x[0])

ans_li = [] # [[start, end], [start, end] ... [start, end]]

for i in range(N-1, -1, -1):
    # ans_li에 정렬된 마지막 원소 리스트 삽입
    if not ans_li:  # N-1 
        ans_li.append(li[i])
        ans_li_idx = 0
    
    # ans_li에 [start] >= li[i] [End]일때 삽입
    # ans_li_idx ++ 을 통하여 다음 값과 비교 
    elif ans_li[ans_li_idx][0] >= li[i][1]:  # (N-2, -1, -1) 부터 처리 
        ans_li.append(li[i])
        ans_li_idx += 1

# print(ans_li)
print(len(ans_li))