import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline()

find_s = 'IOI' + 'OI' * (N-1)

ans = 0
idx = 0
cnt = 0
while idx + 3 <= M:
    if S[idx : idx + 3] == 'IOI': # IOI 패턴 찾기
        idx += 2
        cnt += 1
        # IOI + 뒤에 IOI 가 나오는 횟수를 cnt
        # cnt 가 N이라면, 우리가 찾는 IOI + OI * (N-1)
        if cnt == N:
            ans += 1
            cnt -= 1 # 누적된 IOI 개수를 -1
    
    else:
        idx += 1
        cnt = 0
print(ans)