def solution(d, budget):
    answer = 0
    
    d.sort()
    N = 0  # 누적합 초기화
    
    for cost in d:
        if N + cost > budget:  # 누적합 + 현재 값이 예산을 초과하면 break
            break
        N += cost  # 누적합 갱신
        answer += 1  # 항목 개수 증가
    
    return answer