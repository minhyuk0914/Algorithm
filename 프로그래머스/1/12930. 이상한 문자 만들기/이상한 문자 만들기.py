def solution(s):
    answer = ''
    # 전체 대문자 변경
    s = s.upper()
    s_list = s.split(' ')
    
    for word in s_list:
        for i in range(len(word)):
            if i % 2 != 0:
                answer += word[i].lower()
            else:
                answer += word[i]
        answer += ' '
    return answer[:-1]