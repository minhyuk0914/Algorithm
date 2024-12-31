import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cate_dict = {}


    for _ in range(N):
        name, category = sys.stdin.readline().split()
        
        if category in cate_dict:
            cate_dict[category].append(name)
        else:
            cate_dict[category] = [name]
    # 경우의 수 계산
    ans = 1
    for key in cate_dict:
        ans *= (len(cate_dict[key]) + 1)  # (의상 수 + 1)을 곱함

    ans -= 1  # 알몸인 경우 제외
    print(ans)
