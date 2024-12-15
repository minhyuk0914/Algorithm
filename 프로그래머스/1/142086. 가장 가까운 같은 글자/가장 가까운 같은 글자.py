def solution(s):
    answer = []
    s_dict = {}
    
    for idx, val in enumerate(s):
        if val not in s_dict:
            answer.append(-1)
            s_dict[val] = idx

        else:
            answer.append(idx - s_dict[val])
            s_dict[val] = idx
    
    return answer