def solution(number, limit, power):
    num_list = [0] * (number + 1) # 약수의 개수를 저장할 리스트
    for num in range(1, number + 1):
        # 1부터 루트(num)까지 반복
        for x in range(1, int(num ** 0.5) + 1):
            
            # x가 약수라면
            if num % x == 0:
                num_list[num] += 1
                # 중복을 방지 (제곱수가 아니면 큰 약수도 추가)
                if x != num // x:
                    num_list[num] += 1
                    
    # 제한 조건에 따라 lambda 를 활용해 값 변경
    num_list = list(map(lambda x : power if x > limit else x, num_list))
    
    return sum(num_list)