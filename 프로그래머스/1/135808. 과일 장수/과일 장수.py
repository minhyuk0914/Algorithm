def solution(k, m, score):
    answer = 0
    
    if k < min(score):
        return answer
    else:
        score.sort(reverse = True)
        for i in range(0, len(score), m):
            if len(score[i:i+m]) == m:
                answer += min(score[i:i+m]) * m
        return answer