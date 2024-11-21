import sys

N = int(sys.stdin.readline())

li = []
for i in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))

li.sort()

ans_li = []
for i in range(N-1, -1, -1):
    if not ans_li:  # N-1 
        ans_li.append(li[i])
        ans_li_idx = 0
    elif ans_li[ans_li_idx][0] >= li[i][1]:  # (N-2, -1, -1) 부터 처리 
        ans_li.append(li[i])
        ans_li_idx += 1

# print(ans_li)
print(len(ans_li))