import sys

N = int(sys.stdin.readline())

pos_arr = [] # 양수 x > 0
zero_arr = [] # 0
neg_arr = [] # 음수 x < 0
for i in range(N):
    x = int(sys.stdin.readline())
    
    if x > 0:
        pos_arr.append(x)
    elif x == 0:   # x = 0
        zero_arr.append(x)
    else:   # x < 0
        neg_arr.append(x)

pos_arr.sort()
neg_arr.sort(reverse=True)

# print(pos_arr)
# print(zero_arr)
# print(neg_arr)

# 양수 리스트 계산 x > 0
ans = 0
pos_idx = 0
if len(pos_arr) % 2 != 0:   # 양수 리스트가 홀수개 이면
    ans += pos_arr[0]
    pos_idx += 1
    # print("pos_arr %2 != 0", ans)
for i in range(pos_idx, len(pos_arr)-1, 2):
    if pos_arr[i] == 1 or pos_arr[i+1] == 1:
        ans += pos_arr[i] + pos_arr[i+1]
        i -= 1
        # print("pos_arr elif", ans)
    else:
        ans += pos_arr[i] * pos_arr[i+1]
        # print("pos_arr else", ans)

# 음수 리스트 계산 x < 0
neg_idx = 0
if len(neg_arr) % 2 != 0:
    if len(zero_arr) > 0:   # 양수 리스트가 홀수개 이면
        # ans += neg_arr[0] * zero_arr[0] # 정렬된 음수 중 가장 큰 수 * 0 = 0
        neg_idx += 1
        # print("neg_arr %2 != 0 ", ans)
    else:
        ans += neg_arr[0]
        neg_idx += 1
for i in range(neg_idx, len(neg_arr)-1, 2):
    ans += neg_arr[i] * neg_arr[i+1]
    # print("neg_arr loop", ans)

print(ans)
