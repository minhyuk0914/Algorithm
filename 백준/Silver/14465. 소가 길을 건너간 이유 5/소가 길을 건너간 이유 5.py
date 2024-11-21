import sys

N, K, B = map(int, sys.stdin.readline().split())

li = [0] * N

for i in range(B):
    idx = int(sys.stdin.readline())
    li[idx-1] += 1

# print(li) # [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]


psum = [0] * N
psum[0] = li[0]

for i in range(1, N):
    psum[i] = psum[i-1] + li[i]

# print(psum) # [1, 2, 2, 2, 3, 3, 3, 3, 4, 5]


ans_li = []
for i in range(0, N - K + 1):
    if i == 0:  
        # ans_li[0] == psum[K-1]
        x = psum[i + K - 1] 
    
    else:
        # ans_li[i](i>0) == psum[i + K-1] - psum[i-1]
        # ans_li[2] == psum[2 + 6(K) - 1] - psum[2 - 1]
        # ans_li[2] == psum[7](li[0] ~ li[7]의 합) - psum[1](li[0] ~ li[1]의 합) ==
        # li[2] ~ li[7]의 합 == 1
        x = psum[i + K - 1] - psum[i - 1]

    ans_li.append(x)

# print(ans_li) # [3, 2, 1, 2, 3]
print(min(ans_li)) # 1