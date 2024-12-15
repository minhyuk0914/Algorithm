def solution(s):
    answer = ''
    
    lower_str = []
    upper_str = []
    
    for i in s:
        if i.islower():
            lower_str.append(i)
        else:
            upper_str.append(i)
            
    lower_str.sort(reverse = True)
    upper_str.sort(reverse = True)
    
    answer_list = lower_str + upper_str
    answer = ''.join(answer_list)
    
    return answer