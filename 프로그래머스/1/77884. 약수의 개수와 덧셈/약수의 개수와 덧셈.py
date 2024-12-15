def solution(left, right):
    ans = 0
    
    for val in range(left, right + 1):
        cnt = 0 # 약수의 개수
        # 반복문을 통한 약수의 개수 구하기
        for i in range(1, val + 1):
            if val % i == 0:
                cnt += 1
        # 약수의 개수가 짝수인 경우, + 
        if cnt % 2 == 0:
            ans += val
        # 약수의 개수가 홀수인 경우, - 
        else:
            ans -= val
    return ans