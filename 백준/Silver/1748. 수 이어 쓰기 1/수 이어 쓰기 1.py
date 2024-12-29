import sys

N = int(sys.stdin.readline().strip())

ans = 0
num_len = len(str(N))  # N의 자릿수 계산

# 각 자리수를 순회하며 계산(마지막 자릿수 제외)
for idx in range(1, num_len):
    ans += 9 * 10 ** (idx - 1) * idx

# 마지막 자릿수 처리
ans += (N - 10 ** (num_len - 1) + 1) * num_len
print(ans)