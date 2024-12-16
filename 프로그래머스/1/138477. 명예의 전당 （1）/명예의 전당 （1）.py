def solution(k, score):
    li = []
    answer = []
    for i in score:
        if len(li) < k:
            li.append(i)
            answer.append(min(li))
        elif min(li) < i:
            li.remove(min(li))
            li.append(i)
            answer.append(min(li))
        elif min(li) >= i:
            answer.append(min(li))
            continue
    return answer