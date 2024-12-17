def solution(k, m, score):
    ans = 0
    
    if k < min(score):
        return answer
    else:
        score.sort(reverse = True)
        for i in range(0, len(score), m):
            if len(score[i:i+m]) == m:
                # answer += min(score[i:i+m]) * m
                # 내림차순 정렬을 하였으니, score[i+m-1]의 값 == min(score[i:i+m])값이 동일
                ans += score[i+m-1] * m
        return ans