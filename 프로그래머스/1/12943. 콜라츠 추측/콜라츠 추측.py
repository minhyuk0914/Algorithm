def solution(num):
    cnt = 0
    
    while True:
        # num가 1이 되거나 cnt(횟수)가 500인 경우
        if num == 1 or cnt == 500:
            break
        # 짝수인경우 2로 나눔
        elif num % 2 == 0: 
            num = num / 2
            cnt += 1
        # 짝수가 아닌경우(홀수) 
        else:
            num = (num * 3) + 1 
            cnt += 1
    
    if cnt != 500:
        return cnt
    else:
        return -1
