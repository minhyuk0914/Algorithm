def solution(t, p):
    answer = 0
    len_p = len(p)
    for idx in range(0, len(t) - len_p + 1):
        if t[idx:idx+len_p] <= p:
            answer += 1
    return answer