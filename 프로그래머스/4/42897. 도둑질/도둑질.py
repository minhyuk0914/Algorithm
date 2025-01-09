def solution(money):
    answer = 0
    money_len = len(money)
    
    # 첫 번째 집을 포함하는 경우
    dp_1 = [0] * money_len
    dp_1[0] = money[0]
    dp_1[1] = money[0]
    for i in range(2, money_len - 1): # 마지막 집 제외
        dp_1[i] = max(dp_1[i - 1], money[i] + dp_1[i - 2])
    
    # 첫 번째 집을 선택 x -> 두 번째 집을 선택
    dp_2 = [0] * money_len
    dp_2[0] = 0
    dp_2[1] = money[1]
    for i in range(2, money_len): # 마지막 집 포함
        dp_2[i] = max(dp_2[i - 1], money[i] + dp_2[i - 2])

    return max(dp_1[-2], dp_2[-1]) 
