def solution(arr, divisor):
    answer = []
    
    # x % divisor == 0 인 경우, answer에 삽입
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    
    # 오름차순 정렬
    answer.sort()
    
    # answer 리스트가 있는 경우, 정렬된 리스트 반환
    if answer:
        return answer
    # answer 리스트가 비어있는 경우, [-1] 반환
    else:
        return [-1]