import sys

N, K = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

psum = [0] * N

psum[0] = li[0]
for i in range(1, N):
    psum[i] = psum[i-1] + li[i]

sum_li = []
for i in range(0, N - K + 1):
    if i == 0:
        sum = psum[i + K - 1]
    else:
        sum = psum[i + K - 1] - psum[i-1]

    sum_li.append(sum)

print(max(sum_li))



# sum_li = []

# for i in range(len(li)-K + 1):
#     sum_li.append(sum(li[i:i+K]))

# print(sum_li)
# print(max(sum_li))