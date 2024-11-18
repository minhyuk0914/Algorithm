import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())

    arr = []
    for i in range(N):
        arr.append(list(map(int, sys.stdin.readline().split())))

    arr.sort()

    answer = 0
    max_score = 100000 + 1

    for i in range(N):
        if arr[i][1] < max_score:
            answer += 1
            max_score = arr[i][1]

    print(answer)