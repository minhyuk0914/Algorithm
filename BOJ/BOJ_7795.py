import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())

    a_li = list(map(int, sys.stdin.readline().split()))
    b_li = list(map(int, sys.stdin.readline().split()))

    a_li.sort()
    b_li.sort()

    ans = 0

    a_idx, b_idx = 0, 0

    # print(a_li)
    # print(b_li)
    while a_idx < N:
        if b_idx == M:
            ans += b_idx
            a_idx += 1

        else:
            if a_li[a_idx] > b_li[b_idx]:
                b_idx += 1
            else:
                ans += b_idx
                a_idx += 1
    print(ans)