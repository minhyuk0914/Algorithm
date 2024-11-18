import sys

N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
low, high = max(li), sum(li)    # [영상 최댓값, 영상 총합]

answer = 0

while low <= high:
    mid = (low + high) // 2 
    # 블루레이 강의 넣기
    blueray_num = 1
    total = mid
    for i in range(N):
        if total < li[i]: 
            blueray_num += 1
            total = mid
        
        total -= li[i]

    if blueray_num <= M:
        answer = mid
        high = mid - 1  # [low, mid - 1]
    else:
        low = mid + 1   # [mid + 1, high]

print(answer)
