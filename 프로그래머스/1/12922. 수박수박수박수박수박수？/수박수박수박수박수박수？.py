def solution(n):
    repeat = int(n / 2)
    remain = n % 2
    
    str_1 = '수박'
    str_2 = '수'
    
    answer = str_1 * repeat + str_2 * remain

    return answer